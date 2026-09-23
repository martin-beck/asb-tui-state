---
{
  "branch": "feature/ar-1323-helper-execution-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T01:52:34+00:00",
  "depends_on": [
    "AR-1321"
  ],
  "id": "AR-1323",
  "next_action": "Diagnose and fix the live v1.10 helper-invocation hang against a fresh control state, then rerun connected/unavailable evidence; after that reconcile AR-1323 and continue AR-1327.",
  "owner": "codex-asb-tui-ar1323-20260924",
  "plan": "../plans/AR-1323.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Invoke the approved credential helper through the authenticated runner boundary.",
  "task_revision": 24,
  "title": "Runner-owned credential-helper execution handoff",
  "updated_at": "2026-09-23T23:54:11+00:00",
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

- 2026-09-23T06:43:26+00:00: Rebased PR #137 onto current origin/main to remove an unsigned merge
  commit that failed DCO; preserved helper client, v1.10 negotiation, and inventory fixes as signed
  commits a20585e, 2406630, c7f0f2e. Local UI model generation, 27 tests, and validation pass.

- 2026-09-23T06:46:07+00:00: Reissued the three introduced TUI commits with verified SSH signatures
  using the repository Ed25519 key after hosted policy rejected unsigned commits. New PR #137 head
  is 144ec7e; source and DCO content unchanged.

- 2026-09-23T06:50:05+00:00: TUI PR #137 merged at eddf480. ASB PR #253 branch now includes signed
  current-main merge 1fb8c0a (PR #252 admission repair) so exact protected merge-tree validation can
  proceed; hosted checks are rerunning.

- 2026-09-23T06:51:20+00:00: Hosted policy identified missing Signed-off-by on the signed
  current-main merge; amended merge commit to 79beb05 with SSH signature and DCO trailer, then
  force-pushed. All source changes remain unchanged.

- 2026-09-23T07:00:05+00:00: PR #250 (AR-1326) merged into ASB main at 8692729, causing a provenance
  conflict. Merged current main into PR #253, selected current-main provenance, produced signed+DCO
  merge 51886ff, and pushed. Local auth unit tests hit the known scratch-base overlap guard in /tmp
  worktree; no source failure is inferred.

- 2026-09-23T07:03:04+00:00: Hosted Rust gate exposed provenance drift after AR-1326 merge. Updated
  cli_source_sha256 to exact tested digest 661e6334...f148b4 in signed+DCO commit 8585648; targeted
  workflow_transcript provenance test passes locally.

- 2026-09-23T07:25:27+00:00: ASB PR #253 merged through exact protected merge-tree at 551330b.
  Post-merge hosted workflows started. Live auth enroll/status over the control socket succeeded
  with digest-only receipts. Correctly registered helper vars then exposed a live AuthHelperInvoke
  hang/NeedsReconciliation path; temporary probes/diagnostics were removed and no source changes
  were left.

- 2026-09-23T23:50:28+00:00: Recovered expired claim formerly owned by codex. Recovered abandoned
  lease after live process check found no AR-1323 worker; prior implementation evidence remains in
  task history.

- 2026-09-23T23:52:34+00:00: Claimed by codex-asb-tui-ar1323-20260924.

- 2026-09-23T23:53:38+00:00: Recorded command exit 1; command argv SHA-256
  d8a064fce499433e49430070abe8ab6e3409274402aa0e9dfccda6f61aef7a11.

- 2026-09-23T23:54:01+00:00: Recorded command exit 0; command argv SHA-256
  5c3f125518a6c57b6c9fcbe21c12746f72f46ec00c2d0a73acb919e30e290a52.

- 2026-09-23T23:54:11+00:00: Recorded command exit 1; command argv SHA-256
  150e6ec27951411a9bf84f134de63a192506c089af979dc601b7eeab903d591b.
