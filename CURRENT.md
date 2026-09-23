# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1323](tasks/AR-1323-helper-execution-handoff.md): Runner-owned credential-helper execution handoff | Invoke the approved credential helper through the authenticated runner boundary. | Diagnose and fix the live v1.10 helper-invocation hang against a fresh control state, then rerun connected/unavailable evidence; after that reconcile AR-1323 and continue AR-1327. | codex |

## Open

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1318](tasks/AR-1318-agent-catalog-protocol-compatibility.md): Agent catalog protocol compatibility | Keep asb-tui agent-catalog decoding compatible with the current ASB authenticated schema. | Update the TUI agent-catalog codec/projection for ASB's signer, SBOM, license and target provenance fields, then publish exact fixture evidence. | - |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1195](tasks/AR-1195-cross-repo-wire-compatibility.md): Cross-repository wire compatibility | Prove asb-tui consumes the exact authenticated ASB catalog and lifecycle wire contracts. | Complete independent exact-head review and cross-repository qualification against ASB catalog/lifecycle pins; do not promote while AR-1192 remains unfinished. | - |
| P0 | [AR-1200](tasks/AR-1200-asb-router-client.md): ASB router client adoption | Adopt the authenticated ASB router from the standalone asb-tui lifecycle and UI. | Remain planned until ASB AR-1199 exposes a verified authenticated router; then implement client adoption and paired qualification. | - |
| P0 | [AR-1201](tasks/AR-1201-formal-ui-source-parity.md): Executable formal UI model and source parity | Make every TUI source element and transition mechanically checkable against the formal UI model. | Promote after AR-1197 and inventory prerequisites are reviewed; implement the executable model/source parity manifest and CI gate in asb-tui. | - |
| P0 | [AR-1202](tasks/AR-1202-live-resize-qualification.md): Live terminal resize integration and qualification | Handle terminal resize safely across every asb-tui route without losing state or violating the formal model. | Promote after AR-1201 defines the model binding; review PR #65 at its exact head and implement/qualify live resize in the standalone asb-tui application. | - |

## Done

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Adopt Agent Workflow Quality v0.32.0 | Adopt AWQ v0.32.0 additively in shadow mode while retaining every native gate. | Coordinator must refresh PR #25 on current main, rerun exact-head required hosted checks, and decide whether to promote; retain additive shadow-only scope. | - |
| P0 | [AR-0002](tasks/AR-0002.md): Operationalize asb-tui agent coordination | Operationalize the Git-backed coordinator without disrupting existing asb-tui work. | Rebase both draft candidates onto current main, rerun hosted required checks, and obtain coordinator promotion decision; no merge from review worker. | - |
| P0 | [AR-1192](tasks/AR-1192-authenticated-agent-wizard.md): Authenticated agent wizard integration | Consume authenticated ASB agent catalog and lifecycle in the standalone wizard. | Remain blocked only on ASB AR-1316 authenticated agent-catalog producer; provider, model, authentication, defaults, recording and TUI dispatch contracts are now merged and verified. | - |
| P0 | [AR-1197](tasks/AR-1197-startup-wizard-idempotence.md): Startup wizard readiness and idempotence | Make authoritative startup readiness route into the wizard exactly once when ASB is unconfigured, with deterministic recovery and explanations. | Remain blocked only on authoritative ASB readiness/catalog publication through AR-1316; local startup routing and manual reconfiguration are merged and verified. | - |
| P0 | [AR-1220](tasks/AR-1220-first-run-agent-tutorial.md): asb-tui first-run and first-agent tutorial | Teach first-time users to initialize asb-tui and configure their first agent connection. | Coordinator to monitor PR #107 exact head fb9d4b86270f4be11102868caff226fe35900e78, obtain independent review, and merge only after all required checks pass; then perform post-merge assurance. | - |
| P0 | [AR-1221](tasks/AR-1221-benchmark-readiness-tutorial.md): asb-tui benchmark-readiness tutorial | Teach users to inspect TUI benchmark readiness without performing a run. | Implement the syntax-checked TUI tutorial for testing current agent benchmark readiness. | - |
| P0 | [AR-1222](tasks/AR-1222-tui-run-shared-config.md): asb-tui benchmark run and shared-agent configuration tutorials | Teach TUI users to run a benchmark and apply one configuration to multiple agents. | Coordinator review PR #109 at exact head f607776; merge only after required checks and independent review pass. | - |
| P0 | [AR-1223](tasks/AR-1223-tui-replay-comparison.md): asb-tui record/replay and comparison tutorials | Teach TUI users to replay LLM responses offline and compare multiple agents fairly. | Implement syntax-checked TUI tutorials for LLM record/replay and multi-agent result comparison. | - |
| P0 | [AR-1224](tasks/AR-1224-tutorial-freshness-ci.md): Cross-repository tutorial syntax and freshness gate | Keep asb-tui tutorial routes, actions, commands, and schemas syntactically current in CI. | Implement the cross-repository tutorial discovery and syntax-freshness CI gate after the TUI tutorial contracts are defined. | - |
| P0 | [AR-1317](tasks/AR-1317-secure-wizard-auth-handoff.md): Secure setup-wizard authentication handoff | Complete secure API-key enrollment UX in the setup wizard without raw-key transport. | Continue with AR-1321: connect the documented secure handoff to an approved local credential helper and typed enrollment/status projection. | - |
| P0 | [AR-1321](tasks/AR-1321-credential-helper-bridge.md): Credential-helper bridge for setup wizard | Connect the setup wizard to an approved local credential helper without raw-key transport. | Continue with AR-1323 for negotiated runner-owned helper invocation; PR #134 merged the strict digest-only receipt codec and PR #136 now projects runner-authored auth status before configuration apply. | - |
| P1 | [AR-1198](tasks/AR-1198-help-catalog-ci-hardening.md): Contextual-help catalog CI hardening | Make document-backed contextual help complete, meaningful, privacy-safe, and continuously enforced by CI. | Complete final cross-check of help catalog, UI module inventory, formal model, and UI_OWNERS; retain startup readiness/persistence and authenticated catalog/lifecycle blockers. | - |
| P1 | [AR-1225](tasks/AR-1225-coverage-hardening-post-merge.md): Coverage hardening post-merge assurance | Qualify asb-tui coverage hardening after merge. | Record the exact post-merge workflow run IDs and keep the task open if any required assurance is pending or fails. | - |
| P1 | [AR-1227](tasks/AR-1227-formal-model-foundation-post-merge.md): Formal UI model foundation post-merge assurance | Qualify the corrected formal UI model foundation after merge. | Record exact post-merge workflow evidence for corrected PR #70. | - |
| P1 | [AR-1228](tasks/AR-1228-formal-ownership-ci-post-merge.md): Formal ownership CI post-merge assurance | Qualify formal UI ownership CI after merge. | Record exact post-merge workflow conclusions for corrected PR #71. | - |
| P1 | [AR-1229](tasks/AR-1229-formal-transitions-post-merge.md): Executable formal transitions post-merge assurance | Qualify executable formal UI transitions after merge. | None; retain as immutable post-merge assurance while AR-1201 tracks remaining parity work. | - |
| P1 | [AR-1230](tasks/AR-1230-live-resize-post-merge.md): Live resize post-merge assurance | Qualify live resize state preservation after merge. | None; retain as immutable post-merge assurance while AR-1202 tracks formal resize transition and full route parity. | - |
