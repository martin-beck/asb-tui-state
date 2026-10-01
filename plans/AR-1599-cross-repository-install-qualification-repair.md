# AR-1599 — cross-repository development install qualification repair

Replace the stale blocked qualification attempt with a reproducible,
disposable fresh-user journey for `asb tui install`: default `dev` channel,
current ASB/asb-tui main resolution, temporary clone/build, atomic handoff of
the launcher and required runtime files, launch/status/upgrade/remove, and
offline/network failure handling.  Discover the trusted Cargo/toolchain path
without hard-coded `/usr/bin/cargo`, bind every result to exact source/tree
identities, and preserve prior installation on failed replacement.

Dependencies: ASB AR-1599, TUI AR-1579, AR-1587, AR-1588.  This supersedes the
blocked execution path of AR-1341 while retaining its acceptance scope.

Required evidence: clean disposable workspace, exact-head provenance,
successful and negative lifecycle runs, cleanup/rollback checks, human output
by default with `--json` available, signed/DCO PR, independent review, hosted
checks, and post-merge verification.  Development warnings for missing auth,
signatures, or key management are visible but non-blocking; production remains
fail-closed.
