---
{
  "branch": "feature/ar1187-startup-idempotence",
  "checkpoint_commit": "6d58181810774d48102eb32bb370a21b101f611f",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1197",
  "next_action": "ASB readiness contract AR-1227/AR-1199 is still unpublished; retain the verified local readiness seam and resume authoritative provider wiring when that contract is merged.",
  "owner": "",
  "plan": "../plans/AR-1197.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Make authoritative startup readiness route into the wizard exactly once when ASB is unconfigured, with deterministic recovery and explanations.",
  "task_revision": 34,
  "title": "Startup wizard readiness and idempotence",
  "updated_at": "2026-09-16T11:31:03+00:00",
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

- 2026-09-15T13:04:12+00:00: PR #94 merged through protected path: exact reviewed head
  066d60329a1cb5eda863140dbb513ce0f9ea16dd, merge commit d9a94c37006cdcd9b8629c37de273f80fbf8ef91.
  Exact-head Repository quality run 34972109884 passed. Post-merge Trusted main 34972405476 and
  Repository quality 34972405506 both passed for merge SHA. WorkspaceState now routes/render-handles
  the wizard, but authoritative readiness caller, persistence, and live ASB endpoint remain open.

- 2026-09-15T13:13:43+00:00: PR #95 merged at immutable asb-tui main SHA
  66c0ad168373169ff59dd094c8619b6aaccbcc3b. Exact-head CI run 34972955082 passed with independent
  review. Required post-merge Trusted main 34973217098 and Repository quality 34973217049 both
  passed for the exact resulting main SHA. Injected readiness seam is verified; concrete ASB
  readiness I/O, persistence/restart, and live backend qualification remain open.

- 2026-09-15T13:19:15+00:00: Recovered expired claim formerly owned by root-startup-readiness.
  Recovered expired coordination lease before recording ASB readiness dependency audit.

- 2026-09-15T13:19:22+00:00: Claimed by root-startup-readiness.

- 2026-09-15T13:19:34+00:00: ASB current-main audit found no authoritative readiness producer: no
  asb capabilities/readiness CLI and no readiness projection in control Capabilities. ASB state
  AR-1227 now records the dependency-gated schema/producer/fixture work. Keep asb-tui injection seam
  and fail-closed behavior; do not infer readiness locally or invent persistence semantics.

- 2026-09-15T14:09:40+00:00: PR #98 fixed live wizard Review completion: Enter now dispatches
  FormalEvent::Complete, synchronizes WizardFormalState, and returns to landing only after
  successful formal transition. Exact head 878cbf7235b83eec9e1cceeef843bac350939d54 (SSH/DCO valid),
  exact-head CI 34979236315 passed, merged at e9d456641546a5e6b7d4262121e3ef751fb0c8f5. Post-merge
  Trusted 34979486786 and Repository quality 34979486795 both succeeded for exact main SHA. This
  remains local UI behavior; no ASB I/O or persistence semantics were invented.

- 2026-09-15T14:24:12+00:00: Recovered expired claim formerly owned by root-startup-readiness.
  Recovering expired claim before recording PR #99 merge and post-merge verification.

- 2026-09-15T14:25:05+00:00: Claimed by root-startup-readiness.

- 2026-09-15T14:25:14+00:00: Merged asb-tui PR #99 at caa06ce0083c072b0bb7a8ba6768dd38226d90e6 from
  exact head dc213b2434267f37bb5ebe9e0f75ca3f3ba8b465; exact CI 34980835636 passed, and post-merge
  Trusted 34981184340 plus Repository quality 34981184372 passed. This adds bounded wizard editing,
  Backspace, visible draft, and catalog-backed contextual help without backend or persistence
  changes.

- 2026-09-15T14:59:29+00:00: Recovered expired claim formerly owned by root-startup-readiness.
  Recovering expired claim before recording configuration persistence merge and post-merge evidence.

- 2026-09-15T14:59:38+00:00: Claimed by root-startup-readiness.

- 2026-09-15T14:59:58+00:00: Merged asb-tui PR #101 at 35c4ece19dfdb2ebde5bebef74de918ad321fa43 from
  exact head e28fd7c27fcebcf967d2de917d4b70bc042f1a57; exact CI 34983800769 passed and post-merge
  Repository quality 34984185016 passed. Trusted verification 34984185141 exposed a rustdoc link
  defect; follow-up PR #102 exact head b779dcdc2585657c6f4cf517681573ac1b6d4764 fixed it, exact CI
  34984797557 passed, and post-merge Trusted 34985066671 plus Repository quality 34985066638 passed.
  The slice provides local atomic draft persistence only; it does not claim ASB acknowledgement or
  startup readiness wiring.

- 2026-09-15T15:39:58+00:00: Recovered expired claim formerly owned by root-startup-readiness.
  Recovered expired claim after wizard catalog PR #103 merged; retain AR until readiness dependency
  and persistence acknowledgement remain.

- 2026-09-15T15:52:01+00:00: Claimed by root-startup-readiness.

- 2026-09-15T15:52:12+00:00: PR #105 merged after independent review and exact PR CI 34990957058.
  Automatic startup routing now uses the formal transition interpreter and remains fail-closed;
  concrete readiness acquisition remains dependency-gated.

- 2026-09-15T21:32:38+00:00: Recovered expired claim formerly owned by root-startup-readiness.
  Recover expired startup-readiness worker lease; no active worker evidence remains

- 2026-09-16T11:29:26+00:00: Claimed by codex-asb-tui-ar1197.

- 2026-09-16T11:30:54+00:00: Standalone origin/main audit completed in isolated worktree: cargo fmt
  --check, cargo clippy --all-targets -- -D warnings, and cargo test --locked all passed (136 unit
  tests plus integration suites). No source change was needed; existing readiness controller and UI
  injection remain deterministic and fail-closed. Integration is blocked on the ASB-owned
  readiness/router contract, not a TUI defect.

- 2026-09-16T11:31:03+00:00: Blocked by ASB-owned readiness/router contract AR-1227/AR-1199;
  standalone TUI implementation is fully tested on origin/main and no safe provider wiring can be
  added until the negotiated contract is published.
