# AR-1585 protocol and bootstrap compatibility

Define and implement the negotiated protocol surface required by the wizard:
catalogs, agent/provider status, configuration, authentication status,
recording lifecycle, validation, and benchmark control. Preserve explicit
minimum-version downgrade behavior, request ordering, response identity and
generation checks, atomic partial-bootstrap failure, and development-only
non-blocking authentication semantics.
