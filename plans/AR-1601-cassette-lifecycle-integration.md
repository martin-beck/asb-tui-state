# AR-1601 — real cassette lifecycle integration

Integrate the TUI record/seal/replay/compare route with the released ASB
cassette control contract through an executable cross-process bridge.  The
typed v1.12 transport bridge is already merged by TUI AR-1582; this AR owns the
missing real lifecycle seam, replacing synthetic replay continuity with
campaign-bound cassette identities, digest-only provenance, exact coverage,
provider-egress-denied offline replay, and clear recovery for malformed or
incomplete inputs.

Dependencies: TUI AR-1602, the merged TUI AR-1582 bridge, ASB AR-1605, and
the paired ASB qualification fixture tracked as ASB AR-1606
(authenticated cassette control backend).  Do not resume implementation until
the ASB backend is merged and independently verified.  Do not weaken the existing wizard,
provider/model selection, privacy, or development non-blocking boundaries.

Required evidence: exact paired backend/frontend record and seal, reopen,
offline replay with network denied, comparison, negative matrix, cleanup,
human-readable default output with `--json`, independent review, hosted checks,
and post-merge qualification.
