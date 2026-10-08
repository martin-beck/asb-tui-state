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


class SupersessionProfileTests(unittest.TestCase):
    """Exercise the generic contract against the real ASB TUI task profile."""

    def test_real_replacement_chain_admits_ar1673_dependency(self) -> None:
        tasks = HANDOFF.all_tasks()
        metadata = {item[1]["id"]: item[1] for item in tasks}
        self.assertEqual("superseded", metadata["AR-1672"]["status"])
        self.assertEqual("AR-1668", metadata["AR-1672"]["superseded_by"])
        self.assertEqual("done", metadata["AR-1668"]["status"])
        self.assertEqual("planned", metadata["AR-1673"]["status"])
        self.assertIn("AR-1672", metadata["AR-1673"]["depends_on"])
        self.assertTrue(HANDOFF.dependency_satisfied("AR-1672", tasks))

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
