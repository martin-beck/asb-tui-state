# AR-1600 — channel-aware install UX qualification

Qualify the TUI’s user-facing channel-aware installer against the ASB
publication contract.  A first-time user should be able to accept the default
`dev` channel, see exact provenance, change the channel explicitly, and receive
typed diagnostics for unavailable channels.  The flow must preserve the prior
installation on failed upgrades and remain human-readable by default with
`--json` for automation.

Dependencies: asb-tui AR-1599, asb-tui AR-1588, and ASB AR-1601.  This gate
does not introduce production authentication or secret-management requirements.

Required evidence: clean-state TUI transcript, exact paired ASB/TUI identities,
install/status/doctor/upgrade/rollback/remove, explicit-channel negative cases,
offline behavior, cleanup, independent review, hosted checks, and post-merge
verification.
