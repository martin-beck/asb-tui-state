# AR-1675 — TUI channel manifest consumption and diagnostics

Consume the ASB manifest without duplicating resolver authority. Show channel,
repository, commit, source/build digest, and development-only status in the
install/status/launch screens and JSON projections. Render stale, malformed,
and unavailable manifests as typed recovery guidance.

Acceptance uses exact paired heads and redacted fixtures, preserving the
development non-blocking authentication and key-management contract.
