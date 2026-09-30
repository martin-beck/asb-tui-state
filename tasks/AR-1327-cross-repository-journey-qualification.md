---
{
  "branch": "feature/ar-1327-cross-repository-journey-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T09:46:11+00:00",
  "depends_on": [
    "AR-1324",
    "AR-1325",
    "AR-1326",
    "AR-1330"
  ],
  "id": "AR-1327",
  "next_action": "Promote after AR-1324, AR-1325, and AR-1326; run the disposable development journey and publish exact evidence with live-provider limits.",
  "owner": "tui-ar1327-dev-20260930",
  "plan": "../plans/AR-1327.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the clean development install-to-comparison journey an asb-tui qualification gate.",
  "task_revision": 3,
  "title": "Cross-repository first-class journey qualification",
  "updated_at": "2026-09-30T06:46:11+00:00",
  "worktree_key": "asb-tui-ar-1327-cross-repository-journey-qualification"
}
---

This is qualification only. It must not claim that local mock or replay
evidence proves external OpenRouter reachability.

- 2026-09-30T06:44:55+00:00: AR-1324, AR-1325, AR-1326 and AR-1330 are done; promote
  development-only journey qualification without authenticated production router or live-provider
  gate.

- 2026-09-30T06:46:11+00:00: Claimed by tui-ar1327-dev-20260930.
