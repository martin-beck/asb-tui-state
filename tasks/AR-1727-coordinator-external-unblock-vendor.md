---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T19:29:21+00:00",
  "depends_on": [
    "AR-1722",
    "AR-1726"
  ],
  "id": "AR-1727",
  "next_action": "Wait for an independently reviewed upstream Coordinator successor to ee68fbd that makes resume require exactly one current-revision pause record with matching task ID and nested step_state status/revision on Git and SQLite; then resync only through sync-development and rerun every AR-1727 gate.",
  "owner": "codex-asb-tui-ar1727-unblock-vendor",
  "plan": "../plans/AR-1727-coordinator-external-unblock-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1727.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the reviewed Coordinator external-unblock lifecycle repair so release-blocked asb-tui qualifications can legally return to open without fabricated pause history.",
  "task_revision": 20,
  "title": "Vendor Coordinator external-unblock repair",
  "updated_at": "2026-10-08T15:29:21+00:00",
  "worktree_key": ""
}
---

## Problem statement

asb-tui AR-1575 is correctly `blocked`, unowned, and externally ready after
AR-1725 completed. The currently vendored Coordinator at
`c2eb41879be4f2d50c6b5650e82339e10d5961d8` documents blocked-to-open but only
implements pause-snapshot `resume`; AR-1575 was released blocked and has no
pause snapshot, so no supported command can reopen it.

Upstream Coordinator AR-0085 repaired the lifecycle with a distinct `unblock`
transition and merged as `ee68fbd31ef5564586e4e81297a175abcaa49c6d`, tree
`77803e514ec9384ec623b5b65deb5356165981ad`. PR #1199 received independent
exact-tree approval, and exact-main Verify run 37791093382 and Formal run
37791093305 passed. This downstream AR must consume that immutable development
revision through the official synchronizer; no vendored file or AR-1575 task
metadata may be patched by hand.

## Required repair

- Synchronize the complete official Coordinator development vendor set from
  exact commit `ee68fbd31ef5564586e4e81297a175abcaa49c6d` and tree
  `77803e514ec9384ec623b5b65deb5356165981ad` using `sync-development`.
- Verify every manifest source/destination, Git blob, SHA-256 digest, file mode,
  version/classification field, and deterministic manifest digest. Preserve
  the asb-tui project binding, Git backend, profile, privacy policy, and all
  task intent.
- Prove `unblock` accepts only exact-revision, unowned, externally blocked
  tasks with unambiguous provenance; preserves `next_action`; increments the
  revision once; creates no fabricated pause session; and allows a subsequent
  ordinary claim.
- Prove genuine pause snapshots remain exclusively restorable with
  `resume --session`, and stale revisions, active leases, current pause
  snapshots, missing/malformed/duplicate/cross-mode provenance, concurrency,
  rollback, and projection failure remain fail-closed.
- Retain AR-1722 supersession-chain behavior and AR-1726 lifecycle-complete
  profile coverage. Run all state tests, vendor/header/privacy/generated-view
  checks, applicable formal models, reconciliation, snapshot, and live doctor.
- Obtain independent exact-head review and terminal-green hosted Coordination
  verification. Development authentication, signatures, DCO, tags, and
  release publication are warning-only; exact content, tests, review, and CI
  are mandatory.

## Downstream completion

After AR-1727 is accepted and released, invoke the newly supported `unblock`
command on exact current AR-1575 revision with a note binding the completed
AR-1725 and Coordinator AR-0085 evidence. Then claim and requalify AR-1575
normally. AR-1727 is not permission to change either product repository.

- 2026-10-08T14:21:20+00:00: Claimed by codex-asb-tui-ar1727-unblock-vendor.

- 2026-10-08T14:21:34+00:00: Recorded command exit 0; command argv SHA-256
  46e5ebc51274802d780cef91b85f09529bded8a814967f1dd9ab78f27b96ca01.

- 2026-10-08T14:23:16+00:00: Recorded command exit 0; command argv SHA-256
  c849eba428f6c9c657706f16cbf9630a8e65fff0924bb21b843172c02c032f94.

- 2026-10-08T14:23:33+00:00: Recorded command exit 1; command argv SHA-256
  4ce99c401c381455610374d223382fbec8097aac7182b8835abde3e68e094211.

- 2026-10-08T14:23:48+00:00: Recorded command exit 0; command argv SHA-256
  4a7efd77fbb00e23c85ef6d8579d538bc9e63aee695d103b44c372673a7fcd5c.

- 2026-10-08T14:24:54+00:00: Recorded command exit 0; command argv SHA-256
  38ee6f4b58d2f1983fed9e7a650e3d8f2e03c85463bdbd15654ac51f91fe25f3.

- 2026-10-08T14:25:17+00:00: Recorded command exit 0; command argv SHA-256
  face1d1edda9fa99369578184d092e4677e4ae2bf0c1eea654deb1d4bec6e4a8.

- 2026-10-08T14:25:33+00:00: Recorded command exit 0; command argv SHA-256
  4a7efd77fbb00e23c85ef6d8579d538bc9e63aee695d103b44c372673a7fcd5c.

- 2026-10-08T14:25:58+00:00: Recorded command exit 0; command argv SHA-256
  d1a849e363da84cb46fd318815ad5bcb9cf3872f5286bb99aca61998e0578163.

- 2026-10-08T14:27:08+00:00: Recorded command exit 1; command argv SHA-256
  31637aefbec1a5f20886cbce2e45eb619c1613f3adc6800dccaf617af3e7ab3c.

- 2026-10-08T14:27:32+00:00: Recorded command exit 0; command argv SHA-256
  ff14110be14702444afa379fdaa34c4666c7d1e468c2ae7bf24921a9c6beacb7.

- 2026-10-08T14:28:29+00:00: Recorded command exit 0; command argv SHA-256
  5187e7a76d5aa21cc82cb5df40535faadc41dc193980610e8bb64192d145de0f.

- 2026-10-08T14:31:04+00:00: Recorded command exit 1; command argv SHA-256
  d957de0f7eb25242f7a8ed94544b3eaac2de73c38c61a84febb97081ed8abb17.

- 2026-10-08T14:31:27+00:00: Recorded command exit 1; command argv SHA-256
  56b2d4699ae3c07493a0f58adf990811363620d58ef56c9e7f80701f85cd4d64.

- 2026-10-08T14:31:49+00:00: Recorded command exit 0; command argv SHA-256
  49422686ca0f1bbde90467035a1fab27cfafa3d3cb45b2d5e3011fef1f823378.

- 2026-10-08T14:32:49+00:00: Acceptance blocked by confirmed upstream resume provenance defects at
  ee68fbd/tree 77803e5. validate_session_record and Git decode accept duplicate same-revision pause
  records, mismatched nested step_state status/revision, and wrong task identity; apply_resume
  reopens in all four cases. SQLite ordinary insertion uniquely blocks only duplicate task/revision,
  not nested semantic mismatch. External unblock itself and immutable AR-1575 r74 fixture tests
  passed, but pause-isolation predicate fails. No candidate was committed or published; AR-1575
  remains blocked and unmodified.

- 2026-10-08T14:32:57+00:00: Blocked on upstream Coordinator resume-provenance repair. Exact ee68fbd
  probe accepted duplicate current-revision pauses, wrong task identity, and nested step_state
  status/revision mismatches; selected Git backend blocks none. Required follow-up must fix and
  hostile-test both Git and SQLite before official resync. No AR-1727 candidate/receipt acceptance
  or AR-1575 unblock was published.

- 2026-10-08T15:29:18+00:00: Upstream Coordinator PR #1200 merged as
  e863b57edc7f7a21b2aff2c7b45ce226e12637d2 tree eee603591b917eeca244425559d7c67bb88a7268; postmerge
  Verify 37800348877 and Formal 37800348812 passed; exact official sync-development recovery
  verified 68 blobs, digests, and modes.

- 2026-10-08T15:29:21+00:00: Claimed by codex-asb-tui-ar1727-unblock-vendor.
