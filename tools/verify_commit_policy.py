# Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.
# SPDX-License-Identifier: MIT

"""Verify SSH signatures and exact author DCO trailers in a revision range."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    """Run one bounded, non-interactive Git query."""
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=check,
        text=True,
        capture_output=True,
        timeout=30,
    )


def revisions(root: Path, revision_range: str) -> tuple[str, ...]:
    """Return every commit in the requested non-empty range."""
    values = tuple(
        git(root, "rev-list", "--reverse", revision_range).stdout.splitlines()
    )
    if not values:
        raise RuntimeError("revision range contains no commits")
    return values


def verify(root: Path, allowed_signers: Path, revision_range: str) -> None:
    """Require an allowed SSH signature and matching DCO trailer per commit."""
    for revision in revisions(root, revision_range):
        identity = git(
            root, "show", "-s", "--format=%an <%ae>", revision
        ).stdout.strip()
        message = git(root, "show", "-s", "--format=%B", revision).stdout.splitlines()
        trailer = f"Signed-off-by: {identity}"
        if message.count(trailer) != 1:
            raise RuntimeError(f"{revision}: expected exactly one matching DCO trailer")
        result = git(
            root,
            "-c",
            "gpg.format=ssh",
            "-c",
            f"gpg.ssh.allowedSignersFile={allowed_signers.resolve()}",
            "verify-commit",
            revision,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(f"{revision}: SSH signature is absent or not allowed")


def main(argv: list[str] | None = None) -> int:
    """Parse the revision range and report policy violations without leaking Git output."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("revision_range")
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument(
        "--allowed-signers",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "policy/allowed_signers",
    )
    args = parser.parse_args(argv)
    try:
        verify(args.root.resolve(), args.allowed_signers, args.revision_range)
    except (RuntimeError, subprocess.SubprocessError) as error:
        print(f"commit policy failed: {error}", file=sys.stderr)
        return 1
    print(f"Verified commit policy for {args.revision_range}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
