# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Regression tests for tracked source-header enforcement."""

from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_source_headers", ROOT / "tools/check_source_headers.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load source-header checker")
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class SourceHeaderTests(unittest.TestCase):
    def test_plain_shebang_and_tla_headers_are_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            values = {
                Path("tool.py"): f"# {CHECKER.COPYRIGHT}\n# {CHECKER.SPDX}\n",
                Path(
                    "tool.sh"
                ): f"#!/bin/sh\n# {CHECKER.COPYRIGHT}\n# {CHECKER.SPDX}\n",
                Path("Model.tla"): (
                    f"---- MODULE Model ----\n\\* {CHECKER.COPYRIGHT}\n\\* {CHECKER.SPDX}\n"
                ),
            }
            for path, value in values.items():
                (root / path).write_text(value)
                self.assertEqual([], CHECKER.check_file(root, path))

    def test_bad_or_duplicate_header_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = Path("tool.py")
            pair = f"# {CHECKER.COPYRIGHT}\n# {CHECKER.SPDX}\n"
            (root / path).write_text(pair + "pass\n" + pair)
            self.assertTrue(CHECKER.check_file(root, path))
            (root / path).write_text("pass\n")
            self.assertTrue(CHECKER.check_file(root, path))

    def test_tracked_selection_is_nul_safe(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            source = root / "source with space.py"
            source.write_text(f"# {CHECKER.COPYRIGHT}\n# {CHECKER.SPDX}\n")
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            self.assertEqual(
                (Path("source with space.py"),), CHECKER.tracked_source_files(root)
            )


if __name__ == "__main__":
    unittest.main()
