---
{
  "branch": "repair/ar-1725-operator-runner-parent-toolchain",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T16:47:28+00:00",
  "depends_on": [
    "AR-1721",
    "AR-1724"
  ],
  "id": "AR-1725",
  "next_action": "Repair tools/run-operator-quickstart.py so it resolves and forwards the validated parent ASB Cargo/Rustup inputs before replacing HOME, add real isolated-HOME and hostile-input regressions, rerun the exact paired public journey, obtain independent review, merge, and verify exact-main CI.",
  "observed_branch": "repair/ar-1725-operator-runner-parent-toolchain",
  "observed_dirty": 2,
  "observed_head": "50acbc4af69480b7fbd34db19520a96ce1190a67",
  "owner": "codex-tui-ar1725-parent-toolchain",
  "plan": "../plans/AR-1725-operator-runner-parent-toolchain.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Keep the public operator quickstart usable under its isolated HOME by propagating the validated parent ASB development toolchain boundary.",
  "task_revision": 7,
  "title": "Operator quickstart parent toolchain propagation repair",
  "updated_at": "2026-10-08T12:57:00+00:00",
  "worktree_key": "asb-tui-ar-1725-operator-runner-parent-toolchain"
}
---

AR-1575 final qualification at ASB
`fd956d857970f039db0a4aad03c9e15e59b13da6` and asb-tui
`50acbc4af69480b7fbd34db19520a96ce1190a67` proved that normal ASB source
materialization, status, doctor, upgrade, removal, and the paired
credential-free journey work after ASB AR-1737 and TUI AR-1654.

The documented `tools/run-operator-quickstart.py` gate still replaces `HOME`
with a disposable root before invoking the parent `asb` binary. It forwards
only the child-facing `ASB_TUI_DEV_RUSTUP_HOME` value. The parent router
resolves `ASB_DEV_CARGO` and `ASB_DEV_RUSTUP_HOME`, so bare `asb tui` fails
before executing the installed TUI with typed `trusted_tool_unavailable`.
The identical exact-head gate passes completely when those two validated
parent inputs are supplied: bare launch returns `development_launched` through
the real 80x24 controlling foreground PTY, and all four wizard, setup,
benchmark, recording/replay, and comparison suites pass. The privacy-safe
control receipt has SHA-256
`48903d51c51a418ec910dea9f09e348febd460802285bbb5952fc8c20b84faef`.

Repair only asb-tui qualification tooling and its tests. Resolve the original
host toolchain boundary before installing the disposable `HOME`, then pass
the bounded values through the parent ASB names while retaining the existing
child-facing TUI handoff. ASB remains responsible for validating ownership,
permissions, symlinks, selected-toolchain consistency, descriptor binding,
and substitution resistance. Do not hard-code a host path, inherit secrets,
weaken hostile-layout failures, add provider access, or change ASB, renderer,
wizard, or runtime behavior. Development authentication, signatures, key
management, and provider credentials remain warning-only and never block this
gate.


- 2026-10-08T12:47:28+00:00: Claimed by codex-tui-ar1725-parent-toolchain.

- 2026-10-08T12:51:49+00:00: Recorded command exit 0; command argv SHA-256
  c88f2c5cde1143c5e65215dcce942641c448a54ef05329764ed7a6c5137e463e.

- 2026-10-08T12:55:40+00:00: Recorded command exit 0; command argv SHA-256
  b748788cb32d5d76b8c77ddde9b3c443c4455947f5471db14cf9e8221f33b4d5.

- 2026-10-08T12:57:00+00:00: Recorded command exit 0; command argv SHA-256
  b748788cb32d5d76b8c77ddde9b3c443c4455947f5471db14cf9e8221f33b4d5.
