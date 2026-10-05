# AR-1714 — Validated development cargo/rustup shim install repair

Own the standalone TUI-side repair and qualification of the development
cargo/rustup shim used when `asb tui install` materializes or builds the
frontend. The shim must resolve tools from an explicit bounded development
tool root, reject hostile symlinks, traversal, non-regular files, and paths
outside the approved root before execution, and emit actionable diagnostics.
It must not turn missing production authentication, signatures, or key
management into a setup blocker for local/mock development.

Acceptance:

1. A clean disposable environment can run the supported `asb tui install`
   command using the validated cargo/rustup shim and then launch bare `asb tui`.
2. Hostile symlink, traversal, non-regular-file, and out-of-root fixtures are
   rejected before mutation; no arbitrary executable is run.
3. Missing development auth/signature/key-management state is warning-only and
   the local/mock setup path remains usable.
4. Exact installed TUI evidence records the product/state heads, shim identity,
   command trace, cleanup, and privacy-safe diagnostics.
5. Focused tests, formal/source checks, privacy checks, AWQ, and hosted state
   verification pass. A product merge without this installed journey does not
   satisfy the AR.
