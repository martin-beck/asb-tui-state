# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## In Progress

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1575](tasks/AR-1575.md): ASB/asb-tui final qualification rerun | Requalify the complete credential-free ASB/asb-tui setup and broker journey at exact heads. | Wait for the ASB env-cleared linker handoff repair (drafted as AR-1737 for authoritative registration) and active TUI AR-1654 controlling-PTY/quit response repair to merge and qualify; then rerun exact paired source-built install, status, bare launch, upgrade, removal, descriptor, broker, offline, and typed-failure evidence. | codex-tui-ar1575-final-qualification |
| P0 | [AR-1722](tasks/AR-1722.md): Coordinator supersession-chain vendor upgrade | Adopt the official coordinator supersession-chain contract so evidence-backed replacement ARs safely satisfy downstream dependencies. | Wait for an official signed Agent Workflow Coordinator tag whose vendor manifest includes tools/tlc_runner.py and the complete formal runtime closure from commit 9e6990d77fd54126ca9bfa8671319b785472c91e or equivalent; then resynchronize and rerun every gate. | codex-tui-ar1722-vendor-upgrade |

## Open

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1673](tasks/AR-1673.md): Paired TUI launch diagnostics consumption | Consume the ASB launch-diagnostics repair and verify the installed TUI preserves development-channel identity and warning-only diagnostics. | After the ASB launch repair is released, run installed PTY and JSON launch negatives against exact paired heads and attach the receipt. | - |

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
| P0 | [AR-1703](tasks/AR-1703.md): Top-level asb tui install and launch qualification | Qualify the complete selection-driven asb-tui journey through the supported `asb tui install` and `asb tui` commands. | Promote only after AR-1575 and AR-1654 prove live materialization and terminal-capable bare launch, plus provider, live-run, and capture/comparison ARs are released; then run the clean-room paired command journey and publish the exact-head receipt. | - |
