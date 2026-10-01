# AR-1580 PTY and inherited-control integration

Add a real PTY integration harness for the built asb-tui and ASB development
backend. Verify terminal capability setup, inherited fd-0 SCM_RIGHTS transfer,
broker negotiation, initial projection, interactive exit, and deterministic
socket/server-worker cleanup on success and bounded failure.
