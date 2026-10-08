---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1722",
    "AR-1726"
  ],
  "id": "AR-1727",
  "next_action": "Vendor exact Coordinator merge ee68fbd through the official development synchronizer, qualify pause/resume and external unblock behavior, obtain independent review, restore hosted state CI, then unblock AR-1575 through the supported command.",
  "owner": "",
  "plan": "../plans/AR-1727-coordinator-external-unblock-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1727.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Adopt the reviewed Coordinator external-unblock lifecycle repair so release-blocked asb-tui qualifications can legally return to open without fabricated pause history.",
  "task_revision": 1,
  "title": "Vendor Coordinator external-unblock repair",
  "updated_at": "2026-10-08T14:22:00+00:00",
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
