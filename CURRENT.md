# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Adopt Agent Workflow Quality v0.32.0 | Adopt AWQ v0.32.0 additively in shadow mode while retaining every native gate. | Coordinator may review draft PR 25 at exact head 2bc987ee0a9ad9b18807989501aca3fe87cab8be and, without worker-side merge, promote it only under repository policy. | codex-asb-tui-awq-v032-20260913 |
| P0 | [AR-0002](tasks/AR-0002.md): Operationalize asb-tui agent coordination | Operationalize the Git-backed coordinator without disrupting existing asb-tui work. | Confirm deterministic hosted CI and independent review at state PR #1 head ea47e506c2533f55bd02a76bc363981dc922d58f; product PR #24 remains green. Do not merge. | codex-asb-tui-coordinator-ops-20260913 |
