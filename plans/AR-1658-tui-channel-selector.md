# AR-1658 — TUI development release-channel selector

Add a first-run and reconfiguration screen for release channel. Omitted choice
selects `dev`; explicit dev/stable/nightly/experimental choices are retained,
shown in status, and passed to ASB without silent fallback. Show exact current-
main provenance and clear unavailable-channel recovery in human and JSON views.

Generated development identities and warning-only credential/signature/key status
are allowed and must not block the prototype.
