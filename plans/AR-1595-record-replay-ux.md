# AR-1595 — record and offline replay UX

Add the simple TUI route for selecting one/all agents and workloads to record,
sealing a cassette, choosing replay/offline mode, and comparing recorded
results. Surface provider egress prevention, missing-cassette, expired-cassette,
and partial-recording outcomes plainly.

Dependencies: AR-1594 and paired ASB AR-1596. Downstream: AR-1596.

Required evidence: real lifecycle interaction, deterministic reports,
human-readable default output with explicit JSON option, bounded cleanup,
signed/DCO PR, independent review, and hosted checks.
