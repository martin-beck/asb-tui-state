---
{
  "branch": "feature/ar-1323-helper-execution-handoff",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1321"
  ],
  "id": "AR-1323",
  "next_action": "Add the negotiated runner-owned helper invocation/status contract and wire the wizard to it without paths, raw secrets, or arbitrary command execution.",
  "owner": "",
  "plan": "../plans/AR-1323.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Invoke the approved credential helper through the authenticated runner boundary.",
  "task_revision": 2,
  "title": "Runner-owned credential-helper execution handoff",
  "updated_at": "2026-09-21T03:50:55+00:00",
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
