---
{
  "branch": "feature/ar-1323-helper-execution-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T08:14:05+00:00",
  "depends_on": [
    "AR-1321"
  ],
  "id": "AR-1323",
  "next_action": "Monitor PR #137 at 438db82 and ASB PR #253 at 975f279 until exact-head checks pass; then rerun live helper invocation and capture first-user wizard connected/unavailable evidence.",
  "owner": "codex",
  "plan": "../plans/AR-1323.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Invoke the approved credential helper through the authenticated runner boundary.",
  "task_revision": 12,
  "title": "Runner-owned credential-helper execution handoff",
  "updated_at": "2026-09-23T06:41:14+00:00",
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

- 2026-09-23T06:14:05+00:00: Claimed by codex.

- 2026-09-23T06:14:52+00:00: Verified TUI head c3855a6af1b84fef1d76aca46faacd9bf6821f8b with cargo
  test --locked: 175 unit tests plus integration suites passed. ASB AR-1324 is merged at 6b06f0e
  with all hosted gates green. Remaining acceptance is live cross-repository runner interaction, not
  codec coverage.

- 2026-09-23T06:34:55+00:00: Live ASB probe exposed two integration defects: ASB auth CLI fixed
  300000ms timeout exceeded negotiated 30000ms (PR #253, commit eeeb05b), and TUI helper transport
  omitted v1.10 from negotiation/codec acceptance (PR #137, commit f6c7a41). TUI full suite and
  targeted helper-version test pass; ASB targeted auth test and clippy pass. Both fixes are open for
  exact-head CI.

- 2026-09-23T06:36:30+00:00: Updated TUI PR #137 with signed current-main merge 1fb059a because it
  was behind; required TUI gates are now running. ASB PR #253 remains exact-head eeeb05b with hosted
  checks running. No merge or AR completion claim yet.

- 2026-09-23T06:39:31+00:00: PR #137 initially failed its formal UI ownership gate because changed
  protocol modules were not classified in the module inventory. Added explicit v1.10 helper
  ownership entries in signed commit 438db82; local UI model validation now passes (8 routes, 27
  elements). Fresh TUI checks are running.

- 2026-09-23T06:41:14+00:00: ASB PR #253 policy/Rust failures were deterministic provenance drift
  from the lib.rs timeout fix, not behavior failures. Refreshed
  docs/examples/asb-cli-workflow-v1.provenance.json in signed commit 975f279; local targeted auth
  test and clippy remain green. Fresh PR checks are required.
