# AR-1737 — repair offline run-control dispatch after TUI readiness

1. Read the complete asb-tui and state development documentation; claim an
   isolated worktree from exact current main.
2. Reproduce ASB's exact inherited-fd/PTY test with the same binary/source/tree
   metadata and capture bounded, privacy-safe evidence.
3. Trace readiness, selection, and Run Control event handling. Identify the
   protocol or state transition that prevents the offline default dispatch.
4. Implement the smallest contract-preserving repair in asb-tui. Add positive
   coverage for dispatch after readiness and negative coverage for premature,
   stale, or malformed dispatch; retain cleanup and fail-closed behavior.
5. Run focused TUI tests, the complete applicable workspace gates, formatting,
   lint, privacy, accessibility, and hosted qualification checks.
6. Obtain independent exact-head review, push only a clean signed-DCO branch,
   wait for terminal-success CI, merge through the established workflow, and
   rerun ASB PR #627's exact check against the merged asb-tui main.

Done requires the exact current-main ASB qualification to pass without changing
its PTY/inherited-fd assertions and a post-merge receipt identifying the exact
asb-tui commit and binary digest.
