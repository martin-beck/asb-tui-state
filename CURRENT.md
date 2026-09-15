# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1197](tasks/AR-1197-startup-wizard-idempotence.md): Startup wizard readiness and idempotence | Make authoritative startup readiness route into the wizard exactly once when ASB is unconfigured, with deterministic recovery and explanations. | Integrate the merged StartupController with authoritative ASB readiness transport, wizard route, persistence/restart behavior, and formal transitions; retain PR #90 post-merge evidence. | root-startup-readiness |
| P1 | [AR-1198](tasks/AR-1198-help-catalog-ci-hardening.md): Contextual-help catalog CI hardening | Make document-backed contextual help complete, meaningful, privacy-safe, and continuously enforced by CI. | Integrate document-backed contextual lookup into visible renderer/help overlay; then complete UI_OWNERS/source-inventory/formal-model parity checks without claiming full coverage early. | root-help-quality |

## Open

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Adopt Agent Workflow Quality v0.32.0 | Adopt AWQ v0.32.0 additively in shadow mode while retaining every native gate. | Coordinator may review draft PR 25 at exact head 2bc987ee0a9ad9b18807989501aca3fe87cab8be and, without worker-side merge, promote it only under repository policy. | - |
| P0 | [AR-0002](tasks/AR-0002.md): Operationalize asb-tui agent coordination | Operationalize the Git-backed coordinator without disrupting existing asb-tui work. | Coordinator-only promotion decision for independently reviewed draft state PR #1 and product PR #24; workers must not merge. | - |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1192](tasks/AR-1192-authenticated-agent-wizard.md): Authenticated agent wizard integration | Consume authenticated ASB agent catalog and lifecycle in the standalone wizard. | Review external ASB AR-1190/1191/1186 dependencies, then promote and claim through handoffctl. | - |
| P0 | [AR-1195](tasks/AR-1195-cross-repo-wire-compatibility.md): Cross-repository wire compatibility | Prove asb-tui consumes the exact authenticated ASB catalog and lifecycle wire contracts. | Complete independent exact-head review and cross-repository qualification against ASB catalog/lifecycle pins; do not promote while AR-1192 remains unfinished. | - |
| P0 | [AR-1200](tasks/AR-1200-asb-router-client.md): ASB router client adoption | Adopt the authenticated ASB router from the standalone asb-tui lifecycle and UI. | Remain planned until ASB AR-1199 exposes a verified authenticated router; then implement client adoption and paired qualification. | - |
| P0 | [AR-1201](tasks/AR-1201-formal-ui-source-parity.md): Executable formal UI model and source parity | Make every TUI source element and transition mechanically checkable against the formal UI model. | Promote after AR-1197 and inventory prerequisites are reviewed; implement the executable model/source parity manifest and CI gate in asb-tui. | - |
| P0 | [AR-1202](tasks/AR-1202-live-resize-qualification.md): Live terminal resize integration and qualification | Handle terminal resize safely across every asb-tui route without losing state or violating the formal model. | Promote after AR-1201 defines the model binding; review PR #65 at its exact head and implement/qualify live resize in the standalone asb-tui application. | - |
| P0 | [AR-1220](tasks/AR-1220-first-run-agent-tutorial.md): asb-tui first-run and first-agent tutorial | Teach first-time users to initialize asb-tui and configure their first agent connection. | Promote after ASB tutorial-contract review; write the syntax-checked asb-tui first-run and first-agent tutorial. | - |
| P0 | [AR-1221](tasks/AR-1221-benchmark-readiness-tutorial.md): asb-tui benchmark-readiness tutorial | Teach users to inspect TUI benchmark readiness without performing a run. | Implement the syntax-checked TUI tutorial for testing current agent benchmark readiness. | - |
| P0 | [AR-1222](tasks/AR-1222-tui-run-shared-config.md): asb-tui benchmark run and shared-agent configuration tutorials | Teach TUI users to run a benchmark and apply one configuration to multiple agents. | Implement syntax-checked TUI tutorials for one benchmark run and extending agents with shared configuration. | - |
| P0 | [AR-1223](tasks/AR-1223-tui-replay-comparison.md): asb-tui record/replay and comparison tutorials | Teach TUI users to replay LLM responses offline and compare multiple agents fairly. | Implement syntax-checked TUI tutorials for LLM record/replay and multi-agent result comparison. | - |
| P0 | [AR-1224](tasks/AR-1224-tutorial-freshness-ci.md): Cross-repository tutorial syntax and freshness gate | Keep asb-tui tutorial routes, actions, commands, and schemas syntactically current in CI. | Implement the cross-repository tutorial discovery and syntax-freshness CI gate after the TUI tutorial contracts are defined. | - |

## Done

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-1225](tasks/AR-1225-coverage-hardening-post-merge.md): Coverage hardening post-merge assurance | Qualify asb-tui coverage hardening after merge. | Record the exact post-merge workflow run IDs and keep the task open if any required assurance is pending or fails. | - |
| P1 | [AR-1227](tasks/AR-1227-formal-model-foundation-post-merge.md): Formal UI model foundation post-merge assurance | Qualify the corrected formal UI model foundation after merge. | Record exact post-merge workflow evidence for corrected PR #70. | - |
| P1 | [AR-1228](tasks/AR-1228-formal-ownership-ci-post-merge.md): Formal ownership CI post-merge assurance | Qualify formal UI ownership CI after merge. | Record exact post-merge workflow conclusions for corrected PR #71. | - |
| P1 | [AR-1229](tasks/AR-1229-formal-transitions-post-merge.md): Executable formal transitions post-merge assurance | Qualify executable formal UI transitions after merge. | None; retain as immutable post-merge assurance while AR-1201 tracks remaining parity work. | - |
| P1 | [AR-1230](tasks/AR-1230-live-resize-post-merge.md): Live resize post-merge assurance | Qualify live resize state preservation after merge. | None; retain as immutable post-merge assurance while AR-1202 tracks formal resize transition and full route parity. | - |
