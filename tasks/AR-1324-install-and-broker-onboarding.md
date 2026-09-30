---
{
  "branch": "feature/ar-1324-install-and-broker-onboarding",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1200"
  ],
  "id": "AR-1324",
  "next_action": "Promote after AR-1200; implement the clean development install, broker negotiation, and recovery route with explicit fixture/warning labels.",
  "owner": "",
  "plan": "../plans/AR-1324.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Make clean development ASB/asb-tui installation and local broker onboarding a selectable first step.",
  "task_revision": 2,
  "title": "Install and broker onboarding",
  "updated_at": "2026-09-30T06:01:58+00:00",
  "worktree_key": "asb-tui-ar-1324-install-and-broker-onboarding"
}
---

The TUI must not become a second installer or protocol authority; it renders
the verified ASB installation/control contract.

- 2026-09-30T06:01:58+00:00: Development-only gate policy now removes paired ASB/production
  prerequisites. AR-1200 is complete at 406a6da; promote clean development install and broker
  onboarding against local fixtures.
