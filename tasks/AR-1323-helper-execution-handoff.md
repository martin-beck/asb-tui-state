---
{
  "branch": "feature/ar-1323-helper-execution-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-21T04:50:58+00:00",
  "depends_on": [
    "AR-1321"
  ],
  "id": "AR-1323",
  "next_action": "Open/qualify the TUI helper client against ASB AR-1324 commit 2953465, then run live first-user wizard acceptance and exact-head post-merge gates.",
  "owner": "codex-ar1323",
  "plan": "../plans/AR-1323.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Invoke the approved credential helper through the authenticated runner boundary.",
  "task_revision": 4,
  "title": "Runner-owned credential-helper execution handoff",
  "updated_at": "2026-09-21T03:51:11+00:00",
  "worktree_key": "asb-tui-ar-1323-helper-execution-handoff"
}
---

AR-1321 now decodes digest-only receipts and projects runner-authored status,
but the user still has to provide the receipt manually. This AR owns the
remaining first-user path: discover an explicitly allowlisted helper through
the negotiated ASB control contract, invoke it in the existing sealed/bounded
credential backend, and return only a typed receipt/result. The TUI must never
execute an arbitrary path or receive a raw credential.

- 2026-09-21T03:50:55+00:00: All dependencies including AR-1321 are reconciled done; negotiated
  helper client implementation can proceed.

- 2026-09-21T03:50:58+00:00: Claimed by codex-ar1323.

- 2026-09-21T03:51:11+00:00: Implemented and tested TUI v1.10 auth_helper_invoke codec and transport
  method in signed commit c3855a6 on the isolated TUI worktree. The profile remains credential-free
  JSON at the frontend boundary and is revalidated as typed ProviderProfileV1 by ASB.
