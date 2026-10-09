# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Project-specific tests for permanent Git authority and dormant SQLite support."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location(
    "asb_tui_handoffctl", TOOLS / "handoffctl.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load handoffctl")
HANDOFF = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HANDOFF)


class GitBackendPolicyTests(unittest.TestCase):
    """Bind project identity and prove normal reads cannot instantiate SQLite."""

    def test_project_identity_and_explicit_backend_agree(self) -> None:
        profile = json.loads((ROOT / ".handoffctl.json").read_text())
        binding = json.loads((ROOT / "coordinator.binding.json").read_text())
        backend = json.loads((ROOT / "coordinator.backend.json").read_text())
        self.assertEqual(
            profile["project_id"],
            binding["project_id"],
            "profile and binding must agree",
        )
        self.assertEqual(
            binding["project_id"],
            backend["project_id"],
            "binding and backend must agree",
        )
        self.assertEqual("git", backend["backend"])
        self.assertEqual("martin-beck/asb-tui-state", binding["state_repository"])
        self.assertEqual("martin-beck/asb-tui", binding["product_repository"])

    def test_vendor_identity_is_exact_release_commit(self) -> None:
        manifest = json.loads((ROOT / "coordinator.vendor.json").read_text())
        self.assertEqual(1, manifest["schema_version"])
        self.assertEqual("v0.4.0", manifest["upstream"]["version"])
        self.assertEqual(
            "712b36ea3d188237cbe8104e70d905094f93a96b",
            manifest["upstream"]["commit"],
        )
        self.assertEqual(79, len(manifest["files"]))

    def test_ar1575_r74_fixture_is_external_blocked_and_claimable_after_unblock(self) -> None:
        source_commit = "6a599085279b8ac637fb6dc2cf4006e902b9f8d4"
        task_blob = subprocess.check_output(  # noqa: S603
            ["git", "show", f"{source_commit}:tasks/AR-1575.md"],
            cwd=ROOT,
        )
        session_blob = subprocess.check_output(  # noqa: S603
            ["git", "show", f"{source_commit}:sessions/AR-1575.jsonl"],
            cwd=ROOT,
        )
        self.assertEqual(
            "21b015beb993bbfc1ba52279ad2e679dd20ced927b40076dabb0532f3cdd31f2",
            hashlib.sha256(task_blob).hexdigest(),
        )
        self.assertEqual(
            "98fd7379f4f17bcccbf0caa2dc739bb27b46a289d92889f56934e37ebe4697b9",
            hashlib.sha256(session_blob).hexdigest(),
        )
        with tempfile.TemporaryDirectory() as directory:
            task_path = Path(directory) / "AR-1575.md"
            task_path.write_bytes(task_blob)
            current, body = HANDOFF.read_task(task_path)
        sessions = [json.loads(line) for line in session_blob.decode().splitlines()]
        self.assertFalse(any(item.get("task_revision") == 74 for item in sessions))

        tasks = HANDOFF.all_tasks()
        self.assertEqual(
            ("blocked", 74, "", ""),
            (
                current["status"],
                current["task_revision"],
                current.get("owner", ""),
                current.get("claim_expires", ""),
            ),
        )
        reopened = deepcopy(current)
        next_action = reopened["next_action"]
        with patch.object(
            HANDOFF,
            "storage_backend",
            return_value=SimpleNamespace(load_session_records=lambda _task: sessions),
        ):
            self.assertEqual("external", HANDOFF._blocked_provenance("AR-1575", 74))
            note = HANDOFF.apply_unblock(
                argparse.Namespace(
                    task="AR-1575",
                    expected_revision=74,
                    note="external prerequisites independently verified",
                ),
                reopened,
                tasks,
            )
        self.assertEqual("external prerequisites independently verified", note)
        self.assertEqual(("open", next_action), (reopened["status"], reopened["next_action"]))

        claim_tasks = [
            (task_path, reopened, body) if meta["id"] == "AR-1575" else item
            for item in tasks
            for _, meta, _ in (item,)
        ]
        with patch.object(HANDOFF, "require_role_admission"):
            HANDOFF.apply_claim(
                argparse.Namespace(task="AR-1575", owner="qualification-worker", lease_minutes=10),
                reopened,
                claim_tasks,
            )
        self.assertEqual(
            ("in_progress", "qualification-worker"),
            (reopened["status"], reopened["owner"]),
        )

    def test_live_ar1575_remains_a_supported_descendant_of_r74(self) -> None:
        current = next(meta for _, meta, _ in HANDOFF.all_tasks() if meta["id"] == "AR-1575")
        self.assertGreaterEqual(current["task_revision"], 74)
        status = current["status"]
        owner = current.get("owner", "")
        claim_expires = current.get("claim_expires", "")
        self.assertIn(status, {"blocked", "open", "in_progress", "done"})
        if status == "in_progress":
            self.assertTrue(owner)
            self.assertTrue(claim_expires)
        else:
            self.assertEqual(("", ""), (owner, claim_expires))
        sessions = HANDOFF.storage_backend().load_session_records("AR-1575")
        self.assertFalse(any(item.get("task_revision") == 74 for item in sessions))

    def test_pause_and_external_unblock_provenance_remain_disjoint(self) -> None:
        task_blob = subprocess.check_output(  # noqa: S603
            [
                "git",
                "show",
                "6a599085279b8ac637fb6dc2cf4006e902b9f8d4:tasks/AR-1575.md",
            ],
            cwd=ROOT,
        )
        with tempfile.TemporaryDirectory() as directory:
            task_path = Path(directory) / "AR-1575.md"
            task_path.write_bytes(task_blob)
            current, _ = HANDOFF.read_task(task_path)
        paused = deepcopy(current)
        paused["next_action"] = "Resume the exact paused operation."
        pause_record = HANDOFF.build_session_record(
            paused,
            "pause",
            "2026-10-08T12:46:38+00:00",
        )
        exact = argparse.Namespace(
            task="AR-1575",
            expected_revision=74,
            note="verified",
        )

        with patch.object(
            HANDOFF,
            "storage_backend",
            return_value=SimpleNamespace(load_session_records=lambda _task: [pause_record]),
        ):
            with self.assertRaisesRegex(RuntimeError, "task is paused"):
                HANDOFF.apply_unblock(exact, deepcopy(current), [])
            resumed = deepcopy(current)
            HANDOFF.apply_resume(
                argparse.Namespace(
                    task="AR-1575",
                    expected_revision=74,
                    session="AR-1575@74",
                    note="resume verified pause",
                ),
                resumed,
                [],
            )
        self.assertEqual(
            ("open", paused["next_action"]),
            (resumed["status"], resumed["next_action"]),
        )

        hostile_histories = (
            ([pause_record, deepcopy(pause_record)], "ambiguous", "ambiguous"),
            (
                [{**pause_record, "step_state": {"status": "open", "task_revision": 74}}],
                "malformed",
                "malformed",
            ),
            (
                [
                    {
                        **pause_record,
                        "step_state": {"status": "blocked", "task_revision": 73},
                    }
                ],
                "malformed",
                "malformed",
            ),
            ([{**pause_record, "task": "AR-1574"}], "ambiguous", "coherent paused"),
        )
        for records, unblock_message, resume_message in hostile_histories:
            with (
                patch.object(
                    HANDOFF,
                    "storage_backend",
                    return_value=SimpleNamespace(
                        load_session_records=lambda _task, value=records: value
                    ),
                ),
                self.assertRaisesRegex(RuntimeError, unblock_message),
            ):
                HANDOFF.apply_unblock(exact, deepcopy(current), [])
            with (
                patch.object(
                    HANDOFF,
                    "storage_backend",
                    return_value=SimpleNamespace(
                        load_session_records=lambda _task, value=records: value
                    ),
                ),
                self.assertRaisesRegex(RuntimeError, resume_message),
            ):
                HANDOFF.apply_resume(
                    argparse.Namespace(
                        task="AR-1575",
                        expected_revision=74,
                        session="AR-1575@74",
                        note="reject hostile pause provenance",
                    ),
                    deepcopy(current),
                    [],
                )

        with (
            patch.object(
                HANDOFF,
                "storage_backend",
                return_value=SimpleNamespace(load_session_records=lambda _task: []),
            ),
            self.assertRaisesRegex(RuntimeError, "no session snapshot"),
        ):
            HANDOFF.apply_resume(
                argparse.Namespace(
                    task="AR-1575",
                    expected_revision=74,
                    session="AR-1575@74",
                    note="wrong mode",
                ),
                deepcopy(current),
                [],
            )

        for hostile, message in (
            ({**current, "task_revision": 75}, "stale revision"),
            ({**current, "owner": "stale-worker"}, "active claim metadata"),
            (
                {**current, "claim_expires": "2099-01-01T00:00:00+00:00"},
                "active claim metadata",
            ),
        ):
            with self.assertRaisesRegex(RuntimeError, message):
                HANDOFF.apply_unblock(exact, hostile, [])

    def test_git_task_load_never_constructs_or_creates_sqlite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            database = Path(directory) / "coordinator.sqlite3"
            with (
                patch.object(HANDOFF, "DATABASE", database),
                patch.object(
                    HANDOFF,
                    "SQLiteBackend",
                    side_effect=AssertionError("SQLite must remain dormant"),
                ) as sqlite_backend,
            ):
                backend = HANDOFF.storage_backend()
                self.assertEqual("git", backend.name)
                task_ids = {task[1]["id"] for task in HANDOFF.all_tasks()}
                self.assertIn("AR-0002", task_ids)
            sqlite_backend.assert_not_called()
            self.assertFalse(database.exists())
            self.assertEqual([], list(database.parent.glob("coordinator.sqlite3*")))

    def test_repository_contains_no_sqlite_authority_artifacts(self) -> None:
        artifacts = [
            path.relative_to(ROOT)
            for path in ROOT.rglob("coordinator.sqlite3*")
            if ".git" not in path.parts
        ]
        self.assertEqual([], artifacts)


if __name__ == "__main__":
    unittest.main()
