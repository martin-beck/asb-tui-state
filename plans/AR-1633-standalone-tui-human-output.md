# AR-1633 Standalone TUI human-output parity

Make direct asb-tui lifecycle commands human-readable by default, with
explicit `--json` (or the established opt-in JSON spelling) for machine
consumers. Install, status, launch, upgrade, remove, doctor, and typed failure
diagnostics must match the ASB router vocabulary while preserving JSON callers.

Development-only missing authentication, signatures, and key management remain
visible warnings and never block the prototype.
