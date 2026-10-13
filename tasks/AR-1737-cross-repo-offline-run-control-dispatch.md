---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T07:29:52+00:00",
  "depends_on": [],
  "id": "AR-1737",
  "next_action": "Reproduce the exact ASB inherited-fd/PTY qualification against current asb-tui main, repair readiness-to-offline-run-control dispatch, and publish a reviewed PR with terminal-success CI.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-tui-ar1737-offline-dispatch-20261013",
  "plan": "../plans/AR-1737-cross-repo-offline-run-control-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1737.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1737.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the current-main TUI readiness path so an inherited-fd PTY qualification dispatches the offline default run-control action after readiness.",
  "task_revision": 4,
  "title": "Repair offline run-control dispatch after TUI readiness",
  "updated_at": "2026-10-13T04:30:58+00:00",
  "worktree_key": ""
}
---

This AR owns the asb-tui side of the cross-repository qualification failure
reported by ASB PR #627. The current asb-tui main binary reaches readiness in
the inherited-file-descriptor PTY journey, but the offline default Run Control
action is not dispatched and the paired test fails at `tui.rs:6127`.

The repair must preserve the PTY, inherited-fd, source/binary digest, cleanup,
timeout, and fail-closed assertions. Do not fix this by pinning an obsolete
TUI revision, skipping the journey, relaxing timing, or changing ASB metadata.
Record only privacy-safe failure and qualification evidence.

- 2026-10-13: Created from ASB PR #627's repeated hosted failure against
  current asb-tui main (`486d24709d9045d8e4e2d91221db3a754d2fe3b6`).

- 2026-10-13T04:29:50+00:00: User prioritized the P0 current-main inherited-fd PTY
  readiness-to-offline Run Control repair.

- 2026-10-13T04:29:52+00:00: Claimed by codex-asb-tui-ar1737-offline-dispatch-20261013.

- 2026-10-13T04:30:58+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.
