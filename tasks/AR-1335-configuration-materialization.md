---
{
  "branch": "feature/ar-1335-configuration-materialization",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T13:45:03+00:00",
  "depends_on": [
    "AR-1333",
    "AR-1334"
  ],
  "id": "AR-1335",
  "next_action": "Implement visible preflight route/formal-model transition and integrate materialized bundle apply; retain exact-head PR #161 checks.",
  "owner": "tui-ar1335-dev-20260930",
  "plan": "../plans/AR-1335.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Generate and validate all supported ASB configuration files from reviewed TUI selections.",
  "task_revision": 4,
  "title": "ASB configuration materialization and preflight",
  "updated_at": "2026-09-30T11:07:15+00:00",
  "worktree_key": "asb-tui-ar-1335-configuration-materialization"
}
---

This AR owns asb-tui-side configuration materialization only; it does not modify the ASB repository.

- 2026-09-30T10:44:52+00:00: Dependencies AR-1333 and AR-1334 are done; begin configuration
  materialization and preflight.

- 2026-09-30T10:45:03+00:00: Claimed by tui-ar1335-dev-20260930.

- 2026-09-30T11:07:15+00:00: Exact-head repair 0ec8de4 adds catalog membership validation, provider
  review binding, private atomic sync, and focused drift/unknown-selection tests. PR #161 hosted
  checks must rerun; visible preflight/UI integration remains before merge.
