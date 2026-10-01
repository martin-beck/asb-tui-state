# AR-1586 real ASB bootstrap and control journey

Exercise the exact asb-tui binary against a real ASB ControlServer/backend at
the highest mutually supported protocol version. Assert ordered typed
bootstrap requests (generation/runner identity, capabilities, benchmark and
measurement catalogs, history, agent/provider/configuration/recording/auth
status), request IDs and digests, transactional publication, and explicit
capability-unavailable or downgrade behavior. Cover representative setup,
recording, benchmark, and cancellation mutations with development-only
non-blocking authentication and stable fail-closed separation. This is the
real-backend companion to the projection repair in AR-1581.
