# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Project-specific tests for permanent Git authority and dormant SQLite support."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
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

    def test_vendor_identity_is_exact_development_commit(self) -> None:
        manifest = json.loads((ROOT / "coordinator.vendor.json").read_text())
        self.assertEqual(2, manifest["schema_version"])
        self.assertEqual("development", manifest["upstream"]["channel"])
        self.assertEqual("v0.3.57", manifest["upstream"]["version"])
        self.assertEqual(
            "c2eb41879be4f2d50c6b5650e82339e10d5961d8",
            manifest["upstream"]["commit"],
        )
        self.assertEqual(
            "565458ccedfb8cee71f3e8751bc5531de8f8995c",
            manifest["upstream"]["tree"],
        )

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
