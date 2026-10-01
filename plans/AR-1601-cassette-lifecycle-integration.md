# AR-1601 — real cassette lifecycle integration

Integrate the TUI record/seal/replay/compare route with the released ASB
cassette control contract.  Replace synthetic replay continuity with typed
campaign-bound cassette identities, digest-only provenance, exact coverage,
provider-egress-denied offline replay, and clear recovery for malformed or
incomplete inputs.

Dependencies: TUI AR-1582 and ASB AR-1602.  Do not weaken the existing wizard,
provider/model selection, privacy, or development non-blocking boundaries.

Required evidence: exact paired backend/frontend record and seal, reopen,
offline replay with network denied, comparison, negative matrix, cleanup,
human-readable default output with `--json`, independent review, hosted checks,
and post-merge qualification.
