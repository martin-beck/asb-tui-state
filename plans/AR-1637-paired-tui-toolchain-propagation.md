# AR-1637 — Paired TUI toolchain propagation

Track the nested TUI compatibility contract for ASB's validated development
toolchain. No TUI product change is presumed until exact paired evidence shows
one is required.

Acceptance:

- Exact ASB/TUI heads pass nested install, status, launch, restart, upgrade, and remove.
- No ambient PATH, RUSTC, or RUSTUP_HOME is required.
- Development authentication, signatures, and key management remain warning-only.
