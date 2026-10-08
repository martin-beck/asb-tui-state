# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1703](tasks/AR-1703.md): Top-level asb tui install and launch qualification | Qualify the complete selection-driven asb-tui journey through the supported `asb tui install` and `asb tui` commands. | Promote only after AR-1575 and AR-1654 prove live materialization and terminal-capable bare launch, plus provider, live-run, and capture/comparison ARs are released; then run the clean-room paired command journey and publish the exact-head receipt. | codex-tui-ar1703-clean-room-20261009 |
| P1 | [AR-1728](tasks/AR-1728-dependabot-action-pin-repair.md): Rebuild Dependabot action-pin update on current main | Integrate the taiki-e/install-action pin update carried by stale DCO-invalid Dependabot PR #288 without weakening signature, DCO, exact-main, or independent-review requirements. | Reproduce Dependabot PR #288's reviewed one-line immutable action-pin update from exact current main with project-compliant SSH signature and matching DCO, then independently review, merge, verify exact-main CI, and close the superseded Dependabot PR. | codex-tui-ar1728-action-pin-20261009 |

## Blocked

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1341](tasks/AR-1341.md): Development channel cross-repository qualification | Qualify the cross-repository development release-channel journey. | Qualify the default-dev clone/build/install/launch journey against exact ASB and asb-tui main heads, including failure and cleanup paths. | - |
| P0 | [AR-1345](tasks/AR-1345.md): ASB/asb-tui exact-head final qualification | Qualify the complete current-main ASB and asb-tui development journey at exact heads. | Promote and run exact-head cross-project qualification against ASB 852dcb1 and asb-tui 474f9fc, including credential-free development setup and broker launch. | - |
| P1 | [AR-1665](tasks/AR-1665.md): Paired legacy task-spec metadata vocabulary repair | Record and repair only the historical coordination metadata needed for supported task-spec validation and evidence vocabulary. | Normalize the paired AR-1658 through AR-1664 metadata slice, validate task specs and generated views, and preserve all product and development-only nonblocking semantics. | - |

## Planned

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1685](tasks/AR-1685.md): TUI state spec-acceptance metadata contract | Provide a supported coordinator mutation for recording validated task-spec acceptance before done admission. | Add the supported acceptance mutation, strict validation, and focused coverage without weakening fail-closed done admission. | - |
| P0 | [AR-1686](tasks/AR-1686.md): TUI consumption of content-addressed qualification runner | Consume the ASB content-addressed quickstart runner and prove the TUI preserves valid plan identity through run, capture, replay, and comparison. | Use the ASB plan-create path in the paired TUI acceptance journey and record exact-head positive and stale-identity evidence. | - |
| P0 | [AR-1687](tasks/AR-1687.md): TUI provider-bound comparison qualification | Verify the TUI presents provider-bound comparison availability and confounders truthfully for development/mock runs. | Consume ASB comparison output for available, unavailable, asymmetric, and multi-candidate cases and record privacy-safe TUI evidence. | - |
| P0 | [AR-1689](tasks/AR-1689.md): Paired TUI fresh-user integration and receipt qualification | Qualify the complete fresh-user TUI journey from wizard setup through valid plan, benchmark, recording, offline replay, comparison, and analysis. | Run a disposable exact-head paired journey using plan create and the runner-owned capture/replay routes, then publish a privacy-safe receipt for AR-1613. | - |
