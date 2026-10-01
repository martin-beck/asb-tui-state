# AR-1589 — fresh-user development-channel qualification

Run the complete credential-free fresh-user path at pinned ASB and asb-tui
heads: clone/build, launch the TUI, accept the default `dev` channel, select
agents/providers/authentication/models/defaults, configure recording, run a
small workload, inspect results, and replay/compare offline. Include explicit
channel selection and reconfiguration, stale/malformed identity, failed
materialization, cancellation, and cleanup cases.

The development profile must continue through missing authentication,
signature validation, or key management as visible development warnings using
generated local fixtures. No production security claim is made by this AR;
stable/production paths must remain fail-closed.

Acceptance is a reproducible transcript plus machine-readable evidence,
network-denied replay proof, exact source/executable digests, and independent
review of both repositories' hosted checks.
