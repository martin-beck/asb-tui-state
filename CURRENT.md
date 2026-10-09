# ASB TUI current coordination state

This file is generated. Read `README.md`, then use `tools/handoffctl snapshot`.
Never edit this file directly.

## Open

| Priority | Task | Summary | Next action | Owner |
| --- | --- | --- | --- | --- |
| P0 | [AR-1730](tasks/AR-1730-coordinator-v040-release-vendor.md): Coordinator v0.4.0 release vendor for ASB-TUI compatibility | Adopt the exact Agent Workflow Coordinator v0.4.0 release and qualify ASB-TUI state compatibility without patching vendored bytes or weakening provenance gates. | Promote and claim after state reconciliation; verify upstream v0.4.0 commit/tree and lightweight-tag provenance, then synchronize the exact release through the official vendor path in an isolated state worktree. | - |

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
