# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-0001](tasks/AR-0001.md): Adopt Agent Workflow Quality v0.32.0 | Adopt AWQ v0.32.0 additively in shadow mode while retaining every native gate. | Wait for pre-existing asb-tui agents to finish and reconcile their durable work before claiming. | codex-asb-tui-awq-v032-20260913 |
| P0 | [AR-0002](tasks/AR-0002.md): Operationalize asb-tui agent coordination | Operationalize the Git-backed coordinator without disrupting existing asb-tui work. | Implement deterministic Git-backend state validation and the minimal product contributor pointer in the registered isolated worktrees. | codex-asb-tui-coordinator-ops-20260913 |
