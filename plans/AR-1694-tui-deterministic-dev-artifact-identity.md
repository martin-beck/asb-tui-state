# AR-1694 Deterministic TUI development artifact identity

Make the standalone TUI development materializer reproduce identical executable
bytes across disposable workspace and cargo-home paths, so ASB handoff
manifests validate the actual installed artifact. Preserve source/ref binding,
actual digest validation, trusted toolchain checks, and warning-only development
authentication behavior, with focused repeated-materialization coverage.
