---
{
  "branch": "feature/ar-1335-configuration-materialization",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1333",
    "AR-1334"
  ],
  "id": "AR-1335",
  "next_action": "Promote after provider setup and benchmark selection; implement typed ASB configuration generation, preflight, atomic persistence, and validation.",
  "owner": "",
  "plan": "../plans/AR-1335.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Generate and validate all supported ASB configuration files from reviewed TUI selections.",
  "task_revision": 2,
  "title": "ASB configuration materialization and preflight",
  "updated_at": "2026-09-30T10:44:52+00:00",
  "worktree_key": "asb-tui-ar-1335-configuration-materialization"
}
---

This AR owns asb-tui-side configuration materialization only; it does not modify the ASB repository.

- 2026-09-30T10:44:52+00:00: Dependencies AR-1333 and AR-1334 are done; begin configuration
  materialization and preflight.
