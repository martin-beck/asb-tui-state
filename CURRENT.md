# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1197](tasks/AR-1197-startup-wizard-idempotence.md): Startup wizard readiness and idempotence | Make authoritative startup readiness route into the wizard exactly once when ASB is unconfigured, with deterministic recovery and explanations. | Review PR #87 at the exact head, then integrate it with AR-1187/#76 and the formal wizard model before promotion. | root-ar1197-review |
| P1 | [AR-1198](tasks/AR-1198-help-catalog-ci-hardening.md): Contextual-help catalog CI hardening | Make document-backed contextual help complete, meaningful, privacy-safe, and continuously enforced by CI. | Complete independent review against UI_OWNERS, UI-module inventory, formal model, and all UI routes; PR #88 exact head 74e05d8bb262260f1cef2375ca70800b208bedb6 remains unpromoted. | root-ar-install-router |

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
