---
{
  "branch": "feature/ar-1200-asb-router-client",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T09:52:52+00:00",
  "depends_on": [
    "AR-1195"
  ],
  "id": "AR-1200",
  "next_action": "Remain planned until ASB AR-1199 exposes a verified authenticated router; then implement client adoption and paired qualification.",
  "owner": "tui-ar1200-gate-audit-20260929",
  "plan": "../plans/AR-1200.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt the authenticated ASB router from the standalone asb-tui lifecycle and UI.",
  "task_revision": 3,
  "title": "ASB router client adoption",
  "updated_at": "2026-09-29T09:37:52+00:00",
  "worktree_key": "asb-tui-ar-1200"
}
---

This task is deliberately dependency-gated: protocol-only adapter evidence does not prove an
end-to-end `asb tui install` workflow. Actual UI application and rendering remain here, while
ASB owns only the backend/control route.

- 2026-09-29T09:37:29+00:00: Local AR-1195 dependency is done, but promotion is not authorized: task
  plan still requires external ASB AR-1199 plus AR-1018/1019/1020 verified; no standalone actionable
  task is available.

- 2026-09-29T09:37:52+00:00: Claimed by tui-ar1200-gate-audit-20260929.
