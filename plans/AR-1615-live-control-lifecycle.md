# AR-1615 — live ASB–TUI control handshake and lifecycle repair

Repair and qualify the installed TUI's real ASB control/catalog handoff. The
live route must support record, seal, reopen, replay, compare, retry, cancel,
stale-session, and remove behavior, with typed unavailable/mismatch errors and
an actionable next step. Fixture-only or source-level evidence is insufficient.

Generated development identities are acceptable and missing production
authentication, signatures, or key management must remain non-blocking
warnings. Protocol mismatches and stale handles remain fail-closed.

Required evidence: exact paired heads and protocol digest, live PTY/control
transcript, positive lifecycle path, retry/cancel/stale/remove negatives,
offline activation, no-secret output, independent review, hosted checks, and
exact-main post-merge verification.
