# AR-1613 — current-main release consumption and quickstart qualification

Qualify the standalone TUI from a fresh clone against the published default
`dev` channel after AR-1604 and the paired ASB work are released. Verify that
the integrated installer obtains the current ASB/TUI heads, starts the wizard,
and guides the shortest documented journey: choose provider, authentication,
model, and agents; run a workload; record responses; activate offline replay;
and compare results.

This is a release-consumption qualification, not a replacement for the
wizard, adapter, cassette, or output-contract ARs. Capture exact source heads,
channel metadata, binary versions, commands, and generated artifacts. Missing
credentials, signatures, or key-management services are development-only
warnings and never block this prototype path; production hardening remains
fail-closed.

Required evidence: disposable fresh-clone transcript, selectable/no-copy-paste
wizard path, successful online and offline paths, comparison output, negative
unknown-channel/unavailable-provider cases, no-secret output inspection,
independent review, hosted checks, and exact-main post-merge verification.
