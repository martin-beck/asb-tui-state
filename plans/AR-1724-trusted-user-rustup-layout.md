# AR-1724 — trusted owner Rustup layout and detached quickstart repair

Repair the remaining standalone TUI development-install gap exposed by
AR-1597 at exact main.

## Scope and acceptance

1. Auto-detect the conventional `$HOME/.cargo/bin/cargo -> rustup` shim when
   the shim, Rustup root, settings, selected toolchain, and resolved Cargo and
   Rustc identities are all owned by the effective user and stable. Permit
   group-write only for the bounded owner-controlled Rustup development
   directories/settings/toolchain path already accepted by current ASB.
2. Emit a stable, privacy-safe development warning when that relaxed
   owner-controlled layout is used. It must never qualify stable/production
   trust and must not silently erase the warning across install, status,
   launch, upgrade, or restart.
3. Keep world-writable objects, wrong owners, symlinked settings/toolchain
   components, out-of-root resolution, non-regular executables, executable
   group/other write, replacement races, malformed/oversized settings, and
   cargo/rustc toolchain mismatch fail-closed before mutation or execution.
4. Align the fresh-user wrapper with its current-main runner so an explicit
   exact TUI ref is forwarded for detached qualification checkouts; reject a
   ref that does not resolve to the tested head.
5. Prove the real host-shaped layout without changing host permissions:
   channel compatibility reaches the intended bounded command failure,
   source install and bare launch succeed in a disposable private root, and
   the full credential-free fresh-user journey completes with network denied.
6. Preserve formal UI/source/help ownership boundaries, credential privacy,
   deterministic cleanup, signed+DCO commits, independent review, green hosted
   checks, signed exact-tree merge, and exact-main post-merge validation.

This AR owns only `asb-tui`. Any ASB protocol gap must be recorded separately.

