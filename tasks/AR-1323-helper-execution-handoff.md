---
{
  "branch": "feature/ar-1323-helper-execution-handoff",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1321"
  ],
  "id": "AR-1323",
  "next_action": "Open/qualify the TUI helper client against ASB AR-1324 commit 7165884, then run live first-user wizard acceptance and exact-head post-merge gates.",
  "owner": "",
  "plan": "../plans/AR-1323.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Invoke the approved credential helper through the authenticated runner boundary.",
  "task_revision": 6,
  "title": "Runner-owned credential-helper execution handoff",
  "updated_at": "2026-09-23T06:14:02+00:00",
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

- 2026-09-21T04:00:41+00:00: ASB AR-1324 now includes generated schema updates and passes schema
  conformance; TUI client commit c3855a6 remains fully tested. Cross-repository live qualification
  is next after the independent ASB metrics test blocker is resolved.

- 2026-09-23T06:14:02+00:00: Recovered expired claim formerly owned by codex-ar1323. Recovered
  expired codex-ar1323 claim after confirming no worker process; ASB AR-1324 is merged at 6b06f0e
  and TUI commit c3855a6 is tested. Claiming for cross-repository live acceptance.
