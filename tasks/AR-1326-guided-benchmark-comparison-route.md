---
{
  "branch": "feature/ar-1326-guided-benchmark-comparison-route",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1222",
    "AR-1223",
    "AR-1325",
    "AR-1329"
  ],
  "id": "AR-1326",
  "next_action": "Promote after AR-1222, AR-1223, and AR-1325; implement the selection-driven development campaign and comparison route.",
  "owner": "",
  "plan": "../plans/AR-1326.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Make benchmark, offline replay, and comparison a single guided TUI route.",
  "task_revision": 2,
  "title": "Guided benchmark and comparison route",
  "updated_at": "2026-09-30T06:29:10+00:00",
  "worktree_key": "asb-tui-ar-1326-guided-benchmark-comparison-route"
}
---

This route renders ASB campaign and result contracts; it does not implement a
second runner or provider backend.

- 2026-09-30T06:29:10+00:00: Dependencies AR-1222, AR-1223, and AR-1325 are done; development-only
  gate policy permits implementation without authenticated production router.
