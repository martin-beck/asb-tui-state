# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Unit tests for fail-closed commit signature and DCO policy."""

from __future__ import annotations

import importlib.util
import subprocess
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_commit_policy", ROOT / "tools/verify_commit_policy.py"
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load commit-policy verifier")
POLICY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(POLICY)


def result(stdout: str = "", returncode: int = 0) -> subprocess.CompletedProcess[str]:
    return subprocess.CompletedProcess([], returncode, stdout, "")


class CommitPolicyTests(unittest.TestCase):
    def test_matching_trailer_and_allowed_signature_pass(self) -> None:
        responses = (
            result("abc\n"),
            result("Martin Beck <martin.beck2@gmx.de>\n"),
            result("subject\n\nSigned-off-by: Martin Beck <martin.beck2@gmx.de>\n"),
            result(),
        )
        with patch.object(POLICY, "git", side_effect=responses):
            POLICY.verify(ROOT, ROOT / "policy/allowed_signers", "base..head")

    def test_missing_dco_or_bad_signature_fails_closed(self) -> None:
        missing_dco = (
            result("abc\n"),
            result("A <a@example.com>\n"),
            result("subject\n"),
        )
        with (
            patch.object(POLICY, "git", side_effect=missing_dco),
            self.assertRaisesRegex(RuntimeError, "DCO"),
        ):
            POLICY.verify(ROOT, ROOT / "policy/allowed_signers", "base..head")
        bad_signature = (
            result("abc\n"),
            result("A <a@example.com>\n"),
            result("Signed-off-by: A <a@example.com>\n"),
            result(returncode=1),
        )
        with (
            patch.object(POLICY, "git", side_effect=bad_signature),
            self.assertRaisesRegex(RuntimeError, "signature"),
        ):
            POLICY.verify(ROOT, ROOT / "policy/allowed_signers", "base..head")

    def test_empty_revision_range_is_rejected(self) -> None:
        with (
            patch.object(POLICY, "git", return_value=result()),
            self.assertRaisesRegex(RuntimeError, "no commits"),
        ):
            POLICY.revisions(ROOT, "base..head")


if __name__ == "__main__":
    unittest.main()
