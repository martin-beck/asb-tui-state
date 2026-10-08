# AR-1729 — Race-safe fast noninteractive PTY execution

1. Start from exact public asb-tui main in the registered isolated branch and
   reproduce the specific interleaving where the spawned noninteractive child
   exits before `_open_process_identity` or `tcgetpgrp` can observe it.  Use a
   deterministic synchronization/test hook or purpose-built child fixture;
   iteration-only probability is insufficient.
2. Separate the runner contracts for interactive and noninteractive commands.
   Interactive execution remains fail-closed on live authenticated session,
   controlling-terminal, foreground-group, window-size, readiness, bounded
   input, and cleanup checks.  A noninteractive command that has already exited
   may instead be reaped and have its bounded PTY output/exit status drained and
   classified without demanding a still-live foreground group.
3. Preserve PID/session identity safety.  Never signal an unauthenticated or
   reused PID, never broaden cleanup beyond the fixture session, close every PTY
   descriptor, and retain descendant teardown guarantees when a session was
   authenticated.  Distinguish a legitimate fast exit from a live child that
   failed to acquire the controlling foreground PTY.
4. Add deterministic positive and hostile tests for: exit before identity
   observation; JSON and human install output; nonzero and failing fast exits;
   malformed/no output; live noninteractive child with wrong foreground group;
   interactive readiness/quit; PID-reuse/identity rejection; descriptor and
   descendant cleanup.  Keep the existing repeated fast-output test as stress
   coverage, not as the sole regression proof.
5. Run focused tests plus formatting, Clippy with warnings denied, rustdoc, full
   locked tests, workflow/shell/privacy/provenance gates, formal-model/source
   parity where applicable, and clean-tree verification.  Publish a signed+DCO
   commit and PR, obtain independent exact-head review, merge only the reviewed
   tree, and require exact-main post-merge Repository Quality and Trusted Main
   success before release.

The output is qualification tooling only.  It must not claim that fast process
exit relaxes the actual `asb tui` interactive controlling-terminal contract.

