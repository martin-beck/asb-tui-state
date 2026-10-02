# AR-1636 — Trusted rustc path propagation

Track TUI compatibility with ASB's bounded rustc propagation repair. No TUI
product change is presumed; paired install/lifecycle evidence must be rerun
against the exact ASB repair.

Acceptance:

- Exact TUI current main installs through the repaired ASB dev materializer.
- Full lifecycle and human/JSON diagnostics pass without provider credentials.
- Development authentication, signatures, and key management remain warning-only.
