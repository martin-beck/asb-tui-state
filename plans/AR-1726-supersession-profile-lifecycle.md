# AR-1726 plan: repair supersession profile lifecycle gate

1. Preserve the already completed AR-1673 task and receipt. Reproduce the two
   hosted failures caused by the `open` and then `open|in_progress` assertions.
2. Refactor the focused profile test around a small phase-invariant helper.
   Exercise valid open, valid in-progress, and accepted done metadata plus
   invalid owner, lease, and acceptance combinations.
3. Retain exact AR-1672 to AR-1668 chain assertions and every hostile
   supersession-chain negative without changing coordinator vendor code.
4. Run focused tests, all state tests, vendor/header/privacy/generated-view
   gates, applicable formal verification, reconcile, snapshot, and live
   doctor.
5. Commit only the profile test and AR evidence, obtain independent exact-head
   review, repair any finding, and require terminal-green hosted Coordination
   verification on the final state SHA.
6. Record spec acceptance, release done through handoffctl, reconcile, and
   confirm the post-release head remains green with AR-1673 terminal done.
