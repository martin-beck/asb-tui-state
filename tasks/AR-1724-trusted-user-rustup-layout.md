---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T12:37:58+00:00",
  "depends_on": [
    "AR-1714",
    "AR-1723"
  ],
  "id": "AR-1724",
  "next_action": "Promote and repair TUI development Cargo discovery for the conventional owner-owned Rustup layout, then rerun the detached exact-main fresh-user journey.",
  "owner": "codex-ar1724-rustup-layout-20261008",
  "plan": "../plans/AR-1724-trusted-user-rustup-layout.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Accept the conventional owner-owned group-writable Rustup development layout with an explicit warning while keeping executable and substitution boundaries fail-closed.",
  "task_revision": 7,
  "title": "Trusted owner Rustup layout and detached quickstart repair",
  "updated_at": "2026-10-08T08:39:10+00:00",
  "worktree_key": ""
}
---

AR-1597 exact-main requalification showed that the standalone TUI returns
`development_tool_unavailable` for the current host conventional Rustup shim:
the shim and resolved toolchain executables are regular, owner-controlled and
non-writable by group/other, while owner-controlled Rustup directories and
`settings.toml` use the common group-writable development layout. Current ASB
already accepts this narrow layout with a visible development warning.

Repair only the standalone `asb-tui` implementation and qualification tools.
Development authentication, signatures, and key management remain visible
warnings and never block local/mock execution. Do not modify ASB product code.


- 2026-10-08T08:37:55+00:00: Dependencies AR-1714 and AR-1723 are done. AR-1597 exact-main
  reproduction proves the conventional owner-owned Rustup layout and detached-wrapper gaps;
  implement the narrow TUI-only repair with hostile-path rejection.

- 2026-10-08T08:37:58+00:00: Claimed by codex-ar1724-rustup-layout-20261008.

- 2026-10-08T08:38:14+00:00: Recorded command exit 0; command argv SHA-256
  ebb630ca5026e9d1b388242e978e236f440f70b35548843e8a081a9f7f738a81.

- 2026-10-08T08:38:32+00:00: Recorded command exit 0; command argv SHA-256
  fa38fddc44bfcc1230a8ebafa4fdd340651525b4b50c3e6e15e2d8541b1ffa81.

- 2026-10-08T08:38:52+00:00: Recorded command exit 0; command argv SHA-256
  b5e8c5b81a87760c70c2b7a855f6b119e2fe76e5b964c0c87d2d0907788278fb.

- 2026-10-08T08:39:10+00:00: Recorded command exit 0; command argv SHA-256
  a1d18de80fa5f703b1d0f88ead586ab6f97630e1a8ab58551d2697cf9dbb1c0c.
