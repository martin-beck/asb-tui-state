# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P1 | [AR-1734](tasks/AR-1734-contextual-footer-and-key-help.md): Render contextual footer help and current hotkeys | Add a context-sensitive footer and hotkey overlay that explain the highlighted or hovered item and available actions. | Obtain independent exact-head re-review of repaired PR #302 at 226bd174664471810476aa02dcef86a332f2ee15, wait for hosted checks, and repair any new findings before merge. | codex-asb-tui-ar1734-context-help-20261013 |

## Blocked

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1686](tasks/AR-1686.md): TUI consumption of content-addressed qualification runner | Consume the ASB content-addressed quickstart runner and prove the TUI preserves valid plan identity through run, capture, replay, and comparison. | Rerun the exact paired TUI consumer qualification after ASB AR-1686 lands. | - |
| P1 | [AR-1665](tasks/AR-1665.md): Paired legacy task-spec metadata vocabulary repair | Record and repair only the historical coordination metadata needed for supported task-spec validation and evidence vocabulary. | Normalize the paired AR-1658 through AR-1664 metadata slice, validate task specs and generated views, and preserve all product and development-only nonblocking semantics. | - |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1685](tasks/AR-1685.md): TUI state spec-acceptance metadata contract | Provide a supported coordinator mutation for recording validated task-spec acceptance before done admission. | Add the supported acceptance mutation, strict validation, and focused coverage without weakening fail-closed done admission. | - |
| P0 | [AR-1687](tasks/AR-1687.md): TUI provider-bound comparison qualification | Verify the TUI presents provider-bound comparison availability and confounders truthfully for development/mock runs. | Consume ASB comparison output for available, unavailable, asymmetric, and multi-candidate cases and record privacy-safe TUI evidence. | - |
| P0 | [AR-1689](tasks/AR-1689.md): Paired TUI fresh-user integration and receipt qualification | Qualify the complete fresh-user TUI journey from wizard setup through valid plan, benchmark, recording, offline replay, comparison, and analysis. | Run a disposable exact-head paired journey using plan create and the runner-owned capture/replay routes, then publish a privacy-safe receipt for AR-1613. | - |
| P1 | [AR-1735](tasks/AR-1735-visual-route-and-resize-regression.md): Qualify visual fidelity across routes, resize, and terminal capabilities | Qualify the visual fidelity contract across every route, terminal size, color capability, and keyboard-only interaction without source/model/help drift. | Add deterministic visual-route, resize, accessibility, and formal parity regression coverage for the new fidelity system. | - |
| P1 | [AR-1736](tasks/AR-1736-professional-wizard-fidelity-acceptance.md): Accept professional wizard visual fidelity and usability | Independently qualify that the installed wizard is visually professional, keyboard-discoverable, responsive, and truthful across the complete supported route. | Run an independently reviewed exact-head usability and fidelity acceptance journey across the installed asb-tui wizard. | - |
