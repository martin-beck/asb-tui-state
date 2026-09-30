---
{
  "branch": "feature/ar-1325-first-class-setup-wizard-route",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T08:15:10+00:00",
  "depends_on": [
    "AR-1192",
    "AR-1197",
    "AR-1317",
    "AR-1321",
    "AR-1323",
    "AR-1324",
    "AR-1328"
  ],
  "id": "AR-1325",
  "next_action": "Promote after the helper handoff and development onboarding dependencies are done; bind wizard screens to the local setup contract and add restart/cancellation evidence.",
  "owner": "tui-ar1325-dev-20261001",
  "plan": "../plans/AR-1325.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Deliver a selection-driven first-run and reconfiguration wizard over the shared ASB setup contract.",
  "task_revision": 3,
  "title": "First-class setup wizard route",
  "updated_at": "2026-09-30T06:15:10+00:00",
  "worktree_key": "asb-tui-ar-1325-first-class-setup-wizard-route"
}
---

This is a standalone TUI development route. It must remain wire-compatible with local catalog,
credential-reference, and default-selection fixtures while clearly labeling development evidence.

- 2026-09-30T06:15:08+00:00: Development-only dependency chain is now unblocked: AR-1324 merged at
  dc36b28 and live/production gates were removed from this development workflow. Promote wizard
  route implementation.

- 2026-09-30T06:15:10+00:00: Claimed by tui-ar1325-dev-20261001.
