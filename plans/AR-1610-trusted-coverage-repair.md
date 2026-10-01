# AR-1610 — Trusted-main coverage repair

1. Start from the protected TUI main merge containing AR-1605.
2. Identify uncovered branches in the provider/model/authentication wizard,
   adapter compatibility transaction, and any fixture paths introduced by the
   merge.
3. Add focused deterministic tests that exercise those real branches and keep
   the existing coverage threshold unchanged.
4. Run focused tests, the full locked suite, formatting, clippy, and the exact
   trusted-main coverage command.
5. Obtain independent review, merge the repair, and verify both exact-main
   Repository quality and Trusted-main workflows before releasing AR-1610 and
   closing AR-1605.
