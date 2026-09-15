---
{
  "branch": "feature/ar1187-startup-idempotence",
  "checkpoint_commit": "6d58181810774d48102eb32bb370a21b101f611f",
  "claim_expires": "2026-09-15T12:32:55+00:00",
  "depends_on": [],
  "id": "AR-1197",
  "next_action": "Review PR #87 at the exact head, then integrate it with AR-1187/#76 and the formal wizard model before promotion.",
  "owner": "root-startup-readiness",
  "plan": "../plans/AR-1197.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make authoritative startup readiness route into the wizard exactly once when ASB is unconfigured, with deterministic recovery and explanations.",
  "task_revision": 8,
  "title": "Startup wizard readiness and idempotence",
  "updated_at": "2026-09-15T10:35:13+00:00",
  "worktree_key": "asb-tui-ar-1187-startup-idempotence"
}
---

Complete the standalone asb-tui startup contract from AR-1187. Startup must consume an
authoritative ASB readiness response, auto-open the setup wizard only for explicit
`unconfigured` or `incomplete` states, and remain recoverable without fabricating configuration
for unavailable, malformed, stale, or unauthorized responses. Configured startup must remain on
the landing route while retaining a discoverable manual reconfigure action. Keep all application,
navigation, rendering, and formal-model work in asb-tui; ASB owns only its versioned readiness
contract.

The implementation candidate is PR #87, stacked on the readiness classification in PR #76. PR
#87 exact head is `6d58181810774d48102eb32bb370a21b101f611f`; its parent PR #76 exact head is
`1450df452f066dc14f09bef1e7b1a41ec5128032`. The candidate adds the renderer-neutral
`auto_opens_wizard()` and stable explanations, plus deterministic, idempotence, and fail-closed
tests. It deliberately contains no Ratatui renderer or ASB changes.

Completion also requires integration with the formal AR-1182/1184 state and transition model,
ownership/CI checks, wizard completion confirmation, reconnect/resize/restart behavior, and
TestBackend/model/property evidence for configured, unconfigured, incomplete, unavailable,
malformed, stale, unauthorized, cancel, completion, and manual reconfiguration paths. Do not
promote or merge until exact-head review, hosted CI, SSH signature/DCO checks, and the dependent
wizard work are complete.

- 2026-09-15T08:31:40+00:00: Detailed startup wizard idempotence AR is recorded with exact PR #87
  evidence; begin independent review.

- 2026-09-15T08:31:42+00:00: Claimed by root-ar1197-review.

- 2026-09-15T09:40:54+00:00: Recovered expired claim formerly owned by root-ar1197-review. Recovered
  expired review claim; retain exact PR #87 evidence and reassign before further work.

- 2026-09-15T10:32:55+00:00: Claimed by root-startup-readiness.

- 2026-09-15T10:32:57+00:00: Dependency PR #76 was independently reviewed after rebasing onto
  current asb-tui main 2f47148120c376d2720be7d01fd7869ec3699b24. Guarded force-with-lease updated
  its branch to signed head 250a9e5982456dc869f178d69964b6d6f154e54d. Full cargo test --locked
  --all-targets (103 library tests plus integration/binary suites), fmt, clippy, diff-check and
  clean merge passed. Fresh exact-head CI is now required before merging #76; stacked PR #87 remains
  unqualified until this dependency lands.

- 2026-09-15T10:33:13+00:00: Second independent audit confirms exact head
  250a9e5982456dc869f178d69964b6d6f154e54d is SSH/DCO signed and all local tests (103 unit plus
  integration/binary suites), fmt, clippy --all-features and diff checks pass. Audit notes that this
  is a pure readiness classifier; authoritative ASB response gating, formal model integration and
  guarded configuration application remain acceptance work for stacked PR #87/AR-1197. Hosted
  exact-head Repository quality is in progress.

- 2026-09-15T10:35:13+00:00: Dependency PR #76 merged at immutable asb-tui main SHA
  2faaa21289fe4294df6f6d2c7dd104510647e107 after exact-head CI and independent review. Post-merge
  runs queued: Repository quality 34958715516 and Trusted main verification 34958715501. Keep AR
  in_progress until both terminal; stacked PR #87 remains gated on this dependency and on
  formal/authoritative integration.
