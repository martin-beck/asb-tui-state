---
{
  "branch": "feature/ar-1329-development-provider-setup-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1328"
  ],
  "id": "AR-1329",
  "next_action": "Promote after the setup and enrollment routes are ready; integrate provider/model/default changes, mock-provider validation, and warning-only auth/signature/key-management fallback.",
  "owner": "",
  "plan": "../plans/AR-1329-development-provider-setup-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Integrate development credential lifecycle with provider, model and default selection.",
  "task_revision": 2,
  "title": "Development provider setup integration",
  "updated_at": "2026-09-29T12:55:26+00:00",
  "worktree_key": "asb-tui-ar-1329"
}
---

Keep generated credentials explicitly development-only and preserve the ASB
backend as the authority.

- 2026-09-29T12:55:26+00:00: AR-1328 is merged and post-merge verified; local prerequisite
  satisfied. Promote development provider setup integration.
