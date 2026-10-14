# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1740 — Coordinator v0.7.11 release vendor for ASB-TUI state](tasks/AR-1740-coordinator-v0711-release-vendor.md) | Adopt the exact Agent Workflow Coordinator v0.7.11 release and qualify ASB-TUI state compatibility. | Verify the exact v0.7.11 release identity and vendor the complete allowlisted snapshot through the official synchronizer in an isolated current-main state worktree. | asb-tui-state-ar1740-v0711-20261014 |

## Blocked

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-1665 — Paired legacy task-spec metadata vocabulary repair](tasks/AR-1665.md) | Record and repair only the historical coordination metadata needed for supported task-spec validation and evidence vocabulary. | Normalize the paired AR-1658 through AR-1664 metadata slice, validate task specs and generated views, and preserve all product and development-only nonblocking semantics. | - |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1685 — TUI state spec-acceptance metadata contract](tasks/AR-1685.md) | Provide a supported coordinator mutation for recording validated task-spec acceptance before done admission. | Add the supported acceptance mutation, strict validation, and focused coverage without weakening fail-closed done admission. | - |
| P0 | [AR-1739 — Guided tools, agents, and workloads installation](tasks/AR-1739-guided-tool-agent-workload-installation.md) | Add a guided TUI route that lets users select and install supported tools, coding agents, and workloads through ASB-owned lifecycle operations before setup. | Define and consume the versioned ASB installation catalog and lifecycle contract, then promote when the required ASB command surface is available for the selected current-main pair. | - |
