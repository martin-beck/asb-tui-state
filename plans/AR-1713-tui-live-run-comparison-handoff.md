# AR-1713 — TUI live run, recording, and comparison handoff

Extend the installed `asb tui install` → bare `asb tui` journey with a simple
selection-driven online run route and clear mode labels. Consume ASB's
provider/model readiness, live-run result, recording-catalog, strict replay,
and comparison contracts. Let the user select one/all agents and workloads,
start an explicit live run, choose selected/all recording, then run offline
replay and compare results without another provider call.

Acceptance:

1. TUI presents selectable provider/model/auth readiness and typed missing,
   unavailable, stale, and provider failure states without secrets.
2. Explicit online, local/mock, and offline replay modes remain distinct; a
   live failure never silently falls back.
3. Selected/all capture, digest-only catalog activation, network-denied replay,
   and bounded comparison results are exercised through installed commands.
4. Formal model, help/inventory, PTY, privacy, and hosted checks pass.
