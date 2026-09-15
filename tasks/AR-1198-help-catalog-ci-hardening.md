---
{
  "branch": "feature/ar1037-help-ci-hardening",
  "checkpoint_commit": "74e05d8bb262260f1cef2375ca70800b208bedb6",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1198",
  "next_action": "Complete final cross-check of help catalog, UI module inventory, formal model, and UI_OWNERS; retain startup readiness/persistence and authenticated catalog/lifecycle blockers.",
  "owner": "",
  "plan": "../plans/AR-1198.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Make document-backed contextual help complete, meaningful, privacy-safe, and continuously enforced by CI.",
  "task_revision": 37,
  "title": "Contextual-help catalog CI hardening",
  "updated_at": "2026-09-15T14:59:32+00:00",
  "worktree_key": "asb-tui-ar-1037-help-ci-hardening"
}
---

Implement and qualify the standalone asb-tui help contract from AR-1037 and the related help
catalog work. The catalog must be a versatile, document-backed structure that can be extended for
new screens, elements, actions, and context without scattering prose through rendering code.
Every user-facing UI element and every performable action must resolve to meaningful, plain,
privacy-safe helper text appropriate to its current context; unknown IDs, missing entries, wrong
entry kinds, malformed documents, schema drift, host paths, credentials, and secret-like material
must fail closed.

The implementation candidate is PR #88 at exact head
`74e05d8bb262260f1cef2375ca70800b208bedb6` (asb-tui, based on AR-1037/#61 and related catalog
AR-1036/#60). It changes only help validation/tests and contains no ASB, Ratatui, renderer, or
application implementation. Hosted Repository quality run `34948910240` passed. The candidate
validation commands are `python3 tools/validate-ui-help.py`, `python3 tools/test-ui-help.py`,
`cargo +1.93.0 fmt --all -- --check`, `cargo +1.93.0 clippy --locked --all-targets -- -D warnings`,
and `cargo +1.93.0 test --locked --all-targets`.

Completion requires exact-head review, SSH signature and DCO verification, hosted CI, and
cross-checking the catalog against UI_OWNERS, the UI-module inventory, formal state/elements/
transitions, contextual hotkey/help requirements, and all wizard/landing/configuration/report
routes. CI must detect every newly introduced UI element or action lacking meaningful helper text;
tests must cover schema drift, unknown actions, wrong kinds, private material, missing context,
and deterministic lookup. Do not merge or promote until these checks and durable evidence are
recorded. All actual UI application and rendering work remains in asb-tui.

- 2026-09-15T09:00:00+00:00: Registered from PR #88 at exact head `74e05d8bb262260f1cef2375ca70800b208bedb6`; hosted run `34948910240` passed and the candidate reports the focused/full validation commands above.

- 2026-09-15T08:51:46+00:00: Claimed by root-ar-tui-registry.

- 2026-09-15T08:52:03+00:00: Recorded command exit 0; command argv SHA-256
  0813568ea80c6e65465602e50685396e79e1b48c7baac282f5bff0485d30674c.

- 2026-09-15T08:52:30+00:00: Independent source review: PR #88 exact head
  74e05d8bb262260f1cef2375ca70800b208bedb6 changes only tools/test-ui-help.py and
  tools/validate-ui-help.py; no ASB, Ratatui, renderer, or application implementation. GitHub
  Repository quality run 34948910240 completed SUCCESS. Focused diff covers unknown top-level
  fields, unknown action IDs, wrong action kinds, placeholder/private-material rejection and
  deterministic negative tests. This is evidence for the candidate checks, not proof of complete UI
  inventory synchronization or all-context coverage; those remain acceptance gates.

- 2026-09-15T08:52:32+00:00: Released after exact-head source review and hosted-check verification;
  retain as open until complete UI inventory/formal-model/ownership cross-check and independent
  promotion review.

- 2026-09-15T08:52:55+00:00: Claimed by root-ar-tui-registry.

- 2026-09-15T08:52:58+00:00: Recorded command exit 0; command argv SHA-256
  0813568ea80c6e65465602e50685396e79e1b48c7baac282f5bff0485d30674c.

- 2026-09-15T08:53:05+00:00: Committed the detailed AR-1198 plan through the coordinator run path;
  task remains open for implementation and qualification.

- 2026-09-15T08:53:24+00:00: Claimed by root-ar-tui-registry.

- 2026-09-15T08:53:27+00:00: Recorded command exit 0; command argv SHA-256
  b3dec1b5085e18a9f52742b1d9967de5c621b86d5a8f916764c744d519a523bb.

- 2026-09-15T08:53:34+00:00: Detailed plan is now committed and task remains open.

- 2026-09-15T08:55:29+00:00: Claimed by root-ar-tui-registry.

- 2026-09-15T08:55:31+00:00: Recorded command exit 0; command argv SHA-256
  f76ec0ce25e688dc65b947ead28df8621caeea3940c0c696d5be03b574cac076.

- 2026-09-15T08:55:38+00:00: Recorded command exit 0; command argv SHA-256
  b4ae71776c7c9ee5ba2815b1bca16cf71cef819ed8491fc81a21d0d63d5fa958.

- 2026-09-15T08:55:46+00:00: Recorded AR-1195 exact-head wire adapter evidence through the
  coordinator run path; dependency and planned status remain unchanged.

- 2026-09-15T08:59:47+00:00: Claimed by root-ar-tui-registry.

- 2026-09-15T08:59:50+00:00: Recorded command exit 0; command argv SHA-256
  f76ec0ce25e688dc65b947ead28df8621caeea3940c0c696d5be03b574cac076.

- 2026-09-15T08:59:58+00:00: Recorded command exit 0; command argv SHA-256
  20063deb7250ec655400d952e4febc6360e330698f924bfabcfed67f0b529995.

- 2026-09-15T09:00:05+00:00: Recorded PR #86 exact head, retargeted merge head, and canonical digest
  blocker through the coordinator run path.

- 2026-09-15T09:14:00+00:00: Claimed by root-ar-install-router.

- 2026-09-15T09:14:06+00:00: Recorded command exit 0; command argv SHA-256
  5b15ac3b165f5f1630ebff3aa79708d37d34704d00240816a2bea3c200a4a181.

- 2026-09-15T09:14:20+00:00: Registered dependency-gated AR-1200; release claim without changing
  help task scope.

- 2026-09-15T11:35:14+00:00: Claimed by root-help-quality.

- 2026-09-15T11:35:29+00:00: Corrected help catalog series was rebuilt directly on current asb-tui
  main 8ccf7b93245edbc3477dc4cd681045c428b23cc2. Independent review approved exact candidate
  2a47cd6013226ab33f775c6560179cf17af74ffc; fresh hosted Repository quality run 34963707851
  succeeded. Protected merge of PR #63 produced main 7900471d67d2d24e62a04ff82680aacfb2cfd878;
  post-merge Trusted main 34963906708 and Repository quality 34963906785 both succeeded. The stacked
  historical PR #88 was closed as superseded. Fail-closed action registry discovery and 7-test
  regression coverage are included. Remaining work: actual contextual renderer integration and
  bidirectional UI inventory/formal/owner coverage.

- 2026-09-15T12:14:53+00:00: Recovered expired claim formerly owned by root-help-quality. Recovered
  expired claim to record PR #91 merge and post-merge verification.

- 2026-09-15T12:15:05+00:00: Claimed by root-help-quality.

- 2026-09-15T12:15:17+00:00: PR #91 merged through protected path: exact reviewed head
  1c8d2844292d62ce7f88667d6c41302524a1b1c1, merge commit 2c224fedc62d714d9ac3bde13d0ea8ee10979557.
  Exact-head Repository quality run 34967233705 passed after formal-model ownership and DCO fixes.
  Post-merge Trusted main 34967545564 and Repository quality 34967545751 both passed for merge SHA.
  Runtime catalog remains renderer-neutral; contextual rendering is still open.

- 2026-09-15T12:50:31+00:00: Recovered expired claim formerly owned by root-help-quality. Recovered
  expired help claim to record PR #92 merge, trusted-main failure, and PR #93 remediation.

- 2026-09-15T12:50:39+00:00: Claimed by root-help-quality.

- 2026-09-15T12:50:50+00:00: PR #92 merged as 3dfa81c59b70d6a1db91ed475b96ac6c5b472461 after
  exact-head CI 34969495547; its Trusted main post-merge run 34969778807 failed only at strict 90%
  coverage. Repository quality 34969778754 passed. Follow-up PR #93 added focused wizard coverage,
  merged as 25d9cb4672e2ee707a6d04321ffdeb43733b47ed; exact-head CI 34970601563 passed, and
  post-merge Trusted main 34970832789 plus Repository quality 34970832748 both passed. Wizard
  remains foundational and is not yet wired into the main UI event/render loop.

- 2026-09-15T13:13:27+00:00: Recovered expired claim formerly owned by root-help-quality. Recovered
  expired claim before coordinator update; no active implementation mutation.

- 2026-09-15T13:30:27+00:00: Claimed by root-help-quality.

- 2026-09-15T13:30:40+00:00: PR #96 rebuilt stale PR #81 as a narrow current-main ownership/CI
  synchronization change. Exact base 66c0ad168373169ff59dd094c8619b6aaccbcc3b, exact head
  3df52e118cce6df2c2b163a9d348fb383c37d26c; SSH/DCO verified; hosted quality 34974897999 passed.
  Merged at c8d767e7579f39a13705b97ad31299ca33c2ef3d. Post-merge Trusted 34975160345 and Repository
  quality 34975160356 both succeeded on exact main SHA. Existing help catalog and wizard remain
  intact.

- 2026-09-15T13:45:29+00:00: PR #82 exact head aec7a878e9ea032342b239bbd8f5c77627fe039d passed
  exact-head hosted quality 34976438500 with SSH verification and correctly formatted DCO. It merged
  at 726057316d0149ddce8c957c05a5c543547ec593. Post-merge Trusted main 34976740064 and Repository
  quality 34976740136 both succeeded for that exact main SHA. Change hardens fail-closed
  configuration persistence and records its formal model/inventory ownership; no TUI rendering or
  ASB backend code.

- 2026-09-15T13:59:58+00:00: PR #97 added current-main authoritative measurement catalog projection
  with search/group/item selection coordination, formal model updates, focused tests, and UI
  inventory metadata. Exact head e9436346e05e39346163fafc0eee3cd3552c897e, exact-head CI 34978116964
  passed, merged at 3d8d7ae9d36745933f03b25747122e131cc1706a. Post-merge Trusted 34978387241 and
  Repository quality 34978386914 both passed on exact main SHA.

- 2026-09-15T14:25:23+00:00: Merged asb-tui PR #99 at caa06ce0083c072b0bb7a8ba6768dd38226d90e6 from
  exact head dc213b2434267f37bb5ebe9e0f75ca3f3ba8b465; exact CI 34980835636 and post-merge Trusted
  34981184340 plus Repository quality 34981184372 passed. Wizard help now resolves document-backed
  active-step text via ?/h; formal model, generated artifact, focused CI test, and inventory
  metadata are synchronized.

- 2026-09-15T14:59:32+00:00: Recovered expired claim formerly owned by root-help-quality. Recovering
  expired claim before reconciling post-merge configuration persistence evidence.
