# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""ASB TUI profile integration tests for superseded dependency admission."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location(
    "asb_tui_supersession_handoffctl", TOOLS / "handoffctl.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load handoffctl")
HANDOFF = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(HANDOFF)

Task = tuple[Path, dict[str, Any], str]


def record(task_id: str, status: str, superseded_by: object = None) -> Task:
    """Build the smallest dependency record accepted by dependency_satisfied."""
    metadata: dict[str, Any] = {"id": task_id, "status": status}
    if superseded_by is not None:
        metadata["superseded_by"] = superseded_by
    return Path(f"{task_id}.md"), metadata, ""


def valid_ar1673_phase(metadata: dict[str, Any]) -> bool:
    """Validate the supported downstream lifecycle without pinning one phase."""
    status = metadata.get("status")
    owner = metadata.get("owner", "")
    claim_expires = metadata.get("claim_expires", "")
    if not isinstance(owner, str) or not isinstance(claim_expires, str):
        return False
    if status == "open":
        return owner == "" and claim_expires == ""
    if status == "in_progress":
        return bool(owner) and bool(claim_expires)
    if status != "done" or owner or claim_expires:
        return False

    spec_ref = metadata.get("spec_ref")
    spec_revision = metadata.get("spec_revision")
    acceptance = metadata.get("spec_acceptance")
    evidence_digest = (
        acceptance.get("evidence_digest") if isinstance(acceptance, dict) else None
    )
    return (
        isinstance(spec_ref, str)
        and bool(spec_ref)
        and isinstance(spec_revision, int)
        and spec_revision > 0
        and isinstance(acceptance, dict)
        and acceptance.get("status") == "pass"
        and acceptance.get("spec_ref") == spec_ref
        and acceptance.get("spec_revision") == spec_revision
        and isinstance(acceptance.get("evidence_ref"), str)
        and bool(acceptance.get("evidence_ref"))
        and isinstance(evidence_digest, str)
        and len(evidence_digest) == len("sha256:") + 64
        and evidence_digest.startswith("sha256:")
        and all(character in "0123456789abcdef" for character in evidence_digest[7:])
        and isinstance(acceptance.get("evidence_class"), str)
        and bool(acceptance.get("evidence_class"))
    )


class SupersessionProfileTests(unittest.TestCase):
    """Exercise the generic contract against the real ASB TUI task profile."""

    def test_real_replacement_chain_admits_ar1673_dependency(self) -> None:
        tasks = HANDOFF.all_tasks()
        metadata = {item[1]["id"]: item[1] for item in tasks}
        self.assertEqual("superseded", metadata["AR-1672"]["status"])
        self.assertEqual("AR-1668", metadata["AR-1672"]["superseded_by"])
        self.assertEqual("done", metadata["AR-1668"]["status"])
        self.assertTrue(valid_ar1673_phase(metadata["AR-1673"]))
        self.assertIn("AR-1672", metadata["AR-1673"]["depends_on"])
        self.assertTrue(HANDOFF.dependency_satisfied("AR-1672", tasks))

    def test_ar1673_supported_phases_are_deterministic(self) -> None:
        base: dict[str, Any] = {
            "id": "AR-1673",
            "spec_ref": "specs/AR-1673.json",
            "spec_revision": 1,
        }
        opened = {**base, "status": "open", "owner": "", "claim_expires": ""}
        active = {
            **base,
            "status": "in_progress",
            "owner": "worker-1",
            "claim_expires": "2099-01-01T00:00:00+00:00",
        }
        accepted = {
            **base,
            "status": "done",
            "owner": "",
            "claim_expires": "",
            "spec_acceptance": {
                "status": "pass",
                "spec_ref": base["spec_ref"],
                "spec_revision": base["spec_revision"],
                "evidence_ref": "quality/AR-1673.json",
                "evidence_digest": f"sha256:{'a' * 64}",
                "evidence_class": "contract-test",
            },
        }
        for phase in (opened, active, accepted):
            with self.subTest(status=phase["status"]):
                self.assertTrue(valid_ar1673_phase(phase))

    def test_ar1673_hostile_phase_metadata_fails_closed(self) -> None:
        accepted: dict[str, Any] = {
            "id": "AR-1673",
            "status": "done",
            "owner": "",
            "claim_expires": "",
            "spec_ref": "specs/AR-1673.json",
            "spec_revision": 1,
            "spec_acceptance": {
                "status": "pass",
                "spec_ref": "specs/AR-1673.json",
                "spec_revision": 1,
                "evidence_ref": "quality/AR-1673.json",
                "evidence_digest": f"sha256:{'a' * 64}",
                "evidence_class": "contract-test",
            },
        }
        variants = [
            {**accepted, "status": "open", "owner": "stale-worker"},
            {**accepted, "status": "open", "claim_expires": "stale-lease"},
            {
                **accepted,
                "status": "in_progress",
                "owner": "",
                "claim_expires": "2099-01-01T00:00:00+00:00",
            },
            {
                **accepted,
                "status": "in_progress",
                "owner": "worker-1",
                "claim_expires": "",
            },
            {**accepted, "owner": "stale-worker"},
            {**accepted, "claim_expires": "stale-lease"},
            {key: value for key, value in accepted.items() if key != "spec_acceptance"},
        ]
        for field, value in (
            ("status", "fail"),
            ("spec_ref", "specs/AR-9999.json"),
            ("spec_revision", 2),
            ("evidence_ref", ""),
            ("evidence_digest", "not-a-digest"),
            ("evidence_class", ""),
        ):
            hostile = deepcopy(accepted)
            hostile["spec_acceptance"][field] = value
            variants.append(hostile)

        for metadata in variants:
            with self.subTest(metadata=metadata):
                self.assertFalse(valid_ar1673_phase(metadata))

    def test_invalid_replacement_shapes_fail_closed(self) -> None:
        valid = [record("AR-1672", "superseded", "AR-1668"), record("AR-1668", "done")]
        variants: list[list[Task]] = []

        missing = deepcopy(valid)
        del missing[0][1]["superseded_by"]
        variants.append(missing)
        variants.append([record("AR-1672", "superseded", "bad"), record("AR-1668", "done")])
        variants.append([record("AR-1672", "superseded", "AR-9999")])
        variants.append([record("AR-1672", "superseded", "AR-1672")])
        variants.append(
            [
                record("AR-1672", "superseded", "AR-1668"),
                record("AR-1668", "superseded", "AR-1672"),
            ]
        )
        variants.append(
            [record("AR-1672", "superseded", "AR-1668"), record("AR-1668", "open")]
        )

        for tasks in variants:
            with self.subTest(tasks=tasks):
                self.assertFalse(HANDOFF.dependency_satisfied("AR-1672", tasks))


if __name__ == "__main__":
    unittest.main()
