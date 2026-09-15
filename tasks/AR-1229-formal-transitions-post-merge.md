---
{
  "branch": "feature/ar1184-executable-transitions",
  "checkpoint_commit": "8ccf7b93245edbc3477dc4cd681045c428b23cc2",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1229",
  "next_action": "None; retain as immutable post-merge assurance while AR-1201 tracks remaining parity work.",
  "owner": "",
  "plan": "../plans/AR-1229.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Qualify executable formal UI transitions after merge.",
  "task_revision": 1,
  "title": "Executable formal transitions post-merge assurance",
  "updated_at": "2026-09-15T11:20:00+00:00",
  "worktree_key": "asb-tui-formal-transitions-post-merge"
}
---

PR #74 was rebuilt on current asb-tui main, independently reviewed, and merged at immutable main
SHA `8ccf7b93245edbc3477dc4cd681045c428b23cc2`. The candidate used host ED25519 SSH signing and
DCO trailers. The reviewed fix makes the executable interpreter deserialize focusability metadata
and reject documented non-focusable elements atomically.

- Exact-head Repository quality CI for candidate `58afdbc18466d147caba9f8d9e6a06a7e62a7d42`:
  run `34961950061`, success.
- Local evidence: model validator 7 routes/17 elements, Python model tests 11/11, 112 Rust unit
  tests, all integration/binary suites, format, clippy, and diff checks passed.
- Required exact-main post-merge assurance for `8ccf7b93245edbc3477dc4cd681045c428b23cc2`:
  Repository quality `34962105103` success; Trusted main verification `34962105164` success.

This attestation does not claim complete source/model parity, wizard integration, or renderer/TestBackend
coverage; those remain tracked by AR-1201 and its dependencies.
