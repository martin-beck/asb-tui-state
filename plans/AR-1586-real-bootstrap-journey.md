# AR-1586 TUI ordered bootstrap and control journey

Define and exercise the asb-tui-side ordered bootstrap/control contract at the
highest common protocol version, including generation/runner identity,
capabilities, benchmark and measurement catalogs, history,
agent/provider/configuration/recording/auth status, request IDs and digests,
transactional publication, and explicit capability-unavailable or downgrade
behavior. Cover representative setup, recording, benchmark, and cancellation
mutations with development-only non-blocking authentication and stable
fail-closed separation. Real ASB ControlServer/backend execution is owned by
AR-1587; this AR must not claim synthetic fixtures as cross-repository proof.
