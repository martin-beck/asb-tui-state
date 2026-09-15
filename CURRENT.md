# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## Open

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Adopt Agent Workflow Quality v0.32.0 | Adopt AWQ v0.32.0 additively in shadow mode while retaining every native gate. | Coordinator may review draft PR 25 at exact head 2bc987ee0a9ad9b18807989501aca3fe87cab8be and, without worker-side merge, promote it only under repository policy. | - |
| P0 | [AR-0002](tasks/AR-0002.md): Operationalize asb-tui agent coordination | Operationalize the Git-backed coordinator without disrupting existing asb-tui work. | Coordinator-only promotion decision for independently reviewed draft state PR #1 and product PR #24; workers must not merge. | - |
