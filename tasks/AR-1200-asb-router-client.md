---
{
  "branch": "feature/ar-1200-asb-router-client",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T07:46:36+00:00",
  "depends_on": [
    "AR-1195"
  ],
  "id": "AR-1200",
  "next_action": "Promote and implement the development router client against the local contract fixtures; qualify install/status/upgrade/remove/launch with warning-only development fallback.",
  "owner": "tui-ar1200-dev-20261001",
  "plan": "../plans/AR-1200.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt the ASB development router from the standalone asb-tui lifecycle and UI.",
  "task_revision": 6,
  "title": "ASB development router client adoption",
  "updated_at": "2026-09-30T05:46:36+00:00",
  "worktree_key": "asb-tui-ar-1200"
}
---

This task owns the TUI-side development client and may use local contract fixtures. Actual UI
application and rendering remain here; ASB owns only the backend/control route. Production
authentication and remote trust are explicitly outside this development AR.

- 2026-09-29T09:37:29+00:00: Local AR-1195 dependency is done; the former external authenticated-router
  gate is removed for the development profile. Production trust remains a separate future concern.

- 2026-09-29T09:37:52+00:00: Claimed by tui-ar1200-gate-audit-20260929.

- 2026-09-29T09:38:50+00:00: External paired dependencies remain unmet; released without product
  work and restored planned gate.

- 2026-09-30T05:46:33+00:00: Development-only gate removal is committed at 3c6b6fd; promote local
  fixture-backed router implementation. Production trust remains explicitly out of scope.

- 2026-09-30T05:46:36+00:00: Claimed by tui-ar1200-dev-20261001.
