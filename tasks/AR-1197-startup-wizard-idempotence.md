---
{
  "branch": "feature/ar1187-startup-idempotence",
  "checkpoint_commit": "6d58181810774d48102eb32bb370a21b101f611f",
  "claim_expires": "2026-09-15T13:19:03+00:00",
  "depends_on": [],
  "id": "AR-1197",
  "next_action": "Integrate the merged StartupController with authoritative ASB readiness transport, wizard route, persistence/restart behavior, and formal transitions; retain PR #90 post-merge evidence.",
  "owner": "root-startup-readiness",
  "plan": "../plans/AR-1197.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make authoritative startup readiness route into the wizard exactly once when ASB is unconfigured, with deterministic recovery and explanations.",
  "task_revision": 15,
  "title": "Startup wizard readiness and idempotence",
  "updated_at": "2026-09-15T13:04:03+00:00",
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

- 2026-09-15T10:37:19+00:00: PR #76 merge post-merge assurance completed successfully: Repository
  quality 34958715516 and Trusted main verification 34958715501 both success for main SHA
  2faaa21289fe4294df6f6d2c7dd104510647e107. AR remains in_progress because stacked PR #87 and
  authoritative/formal wizard integration are still outstanding.

- 2026-09-15T10:40:29+00:00: Stacked PR #87 was independently reviewed and guarded-force-updated
  from 6d58181810774d48102eb32bb370a21b101f611f to signed current-main head
  aec416d71b6f1c34b5c45f28cc2d0eadfbca1890. Full local tests (106 unit plus integration/binary
  suites), fmt, clippy, diff-check and clean merge pass. Candidate remains pure startup decision
  logic; authoritative ASB readiness integration, exactly-once state behavior and formal-model
  parity remain acceptance requirements. Fresh hosted exact-head CI is now running.

- 2026-09-15T10:42:41+00:00: PR #87 merged at immutable asb-tui main SHA
  5bf74fa7ce1944b0611f9a03c7f3367d0ee70053 after fresh exact-head CI success and independent review.
  Post-merge runs queued: Repository quality 34959377930 and Trusted main verification 34959377980.
  Keep AR in_progress until both terminal; authoritative ASB response integration and formal-model
  parity remain separate acceptance work.

- 2026-09-15T10:44:50+00:00: Post-merge assurance for 5bf74fa7ce1944b0611f9a03c7f3367d0ee70053
  completed successfully: Trusted main verification 34959377980 and Repository quality 34959377930
  both success. PR #76 and #87 stack is now merged and green; AR remains in_progress because the
  pure classifier/decision layer still needs authoritative ASB readiness integration, exactly-once
  state behavior, and formal-model parity.

- 2026-09-15T11:47:23+00:00: PR #90 exact head was rebased onto current asb-tui main and
  independently re-reviewed. Final head 187282b8580dc7b02bb1a87a90d727b09451afa4 is SSH/DCO signed;
  exact-head Repository quality run 34964685327 succeeded. Protected merge produced main SHA
  6220592e561cbbf56a7920ed6d0a2a079c12ce29. Required post-merge Trusted main verification
  34964955271 and Repository quality 34964955172 both succeeded. The merged controller is a bounded
  renderer-neutral one-shot gate; authoritative ASB readiness I/O, wizard navigation, persistence,
  and complete formal parity remain outstanding.

- 2026-09-15T12:50:28+00:00: Recovered expired claim formerly owned by root-startup-readiness.
  Recovered expired startup-wizard claim during coordinator reconciliation; retained open
  integration work.

- 2026-09-15T13:04:03+00:00: Claimed by root-startup-readiness.
