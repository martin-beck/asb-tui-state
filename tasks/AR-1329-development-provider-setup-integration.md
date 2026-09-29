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
  "status": "done",
  "summary": "Integrate development credential lifecycle with provider, model and default selection.",
  "task_revision": 4,
  "title": "Development provider setup integration",
  "updated_at": "2026-09-29T13:10:40+00:00",
  "worktree_key": "asb-tui-ar-1329"
}
---

Keep generated credentials explicitly development-only and preserve the ASB
backend as the authority.

- 2026-09-29T12:55:26+00:00: AR-1328 is merged and post-merge verified; local prerequisite
  satisfied. Promote development provider setup integration.

- 2026-09-29T12:55:29+00:00: Claimed by tui-ar1329-dev-20260929.

- 2026-09-29T13:10:40+00:00: Merged PR #148 at main 30cfebf10b91ab3490a8e0e7761424e8bacd595e. PR
  quality 36572652972, AWQ shadow 36572653109, post-merge quality 36572943310, trusted main
  36572943366 all succeeded. Added bounded development catalog fallback, live authority replacement,
  formal model/inventory coverage, and regression tests.
