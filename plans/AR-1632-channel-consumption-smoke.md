# AR-1632 Clean-room development-channel consumption smoke

Execute a disposable fresh-clone TUI journey against the ASB dev channel:
install with the default `dev`, launch, restart, upgrade from a pinned older
dev revision, and exercise bounded rollback/tamper diagnostics. Verify both
human-readable output and opt-in `--json` projections.

The runner must resolve and record the exact current asb-tui main/source
identity used for the run; stale hard-coded TUI revisions are not acceptable.
Rollback pins must be explicitly labeled and must not replace the current-main
leg.

Use local/mock generated development fixtures. No missing authentication,
signature validation, or key management may block the prototype.
