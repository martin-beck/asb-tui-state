# AR-1690 TUI development-channel current-main consumption

Bind the TUI materializer and launch handoff to the ASB versioned channel
manifest. Persist the selected channel, display the resolved paired heads, and
provide deterministic diagnostics for stale, digest-mismatched, and unavailable
channels. Keep generated development authenticity and absent provider
credentials as visible warnings only. Add selection-driven PTY and JSON tests
without changing production trust behavior.
