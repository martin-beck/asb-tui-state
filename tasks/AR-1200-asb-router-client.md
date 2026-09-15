---
{
  "branch": "feature/ar-1200-asb-router-client",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1195"],
  "id": "AR-1200",
  "next_action": "Remain planned until ASB AR-1199 exposes a verified authenticated router; then implement client adoption and paired qualification.",
  "owner": "",
  "plan": "../plans/AR-1200.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Adopt the authenticated ASB router from the standalone asb-tui lifecycle and UI.",
  "task_revision": 1,
  "title": "ASB router client adoption",
  "updated_at": "2026-09-15T00:00:00+00:00",
  "worktree_key": "asb-tui-ar-1200"
}
---

This task is deliberately dependency-gated: protocol-only adapter evidence does not prove an
end-to-end `asb tui install` workflow. Actual UI application and rendering remain here, while
ASB owns only the backend/control route.
