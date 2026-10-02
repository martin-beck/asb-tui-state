# AR-1632 Clean-room development-channel consumption smoke

Execute a disposable fresh-clone TUI journey against the ASB dev channel:
install with the default `dev`, launch, restart, upgrade from a pinned older
dev revision, and exercise bounded rollback/tamper diagnostics. Verify both
human-readable output and opt-in `--json` projections.

Use local/mock generated development fixtures. No missing authentication,
signature validation, or key management may block the prototype.
