---
{
  "branch": "feature/ar-1325-first-class-setup-wizard-route",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1192", "AR-1197", "AR-1317", "AR-1321", "AR-1323", "AR-1324"],
  "id": "AR-1325",
  "title": "First-class setup wizard route",
  "next_action": "Promote after the helper handoff and onboarding dependencies are done; bind the wizard screens to the shared setup contract and add restart/cancellation evidence.",
  "owner": "",
  "plan": "../plans/AR-1325.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Deliver a selection-driven first-run and reconfiguration wizard over the shared ASB setup contract.",
  "task_revision": 1,
  "updated_at": "2026-09-25T15:40:00+00:00",
  "worktree_key": "asb-tui-ar-1325-first-class-setup-wizard-route"
}
---

This is the TUI half of ASB AR-1442 and must remain wire-compatible with its
catalog, authentication, and default-selection semantics.
