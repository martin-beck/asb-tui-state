# AR-1740 plan: Coordinator v0.7.11 release vendor for ASB-TUI state

1. Refresh upstream release refs and independently verify the v0.7.11 tag,
   resolved commit, tree, tag object type, source cleanliness, and release
   identity. Record the lightweight-tag boundary without overstating it.
2. Reconcile the state repository and inspect active claims, wrapped commands,
   worktrees, and locks. Proceed only with a clean, quiescent coordinator
   authority; preserve every unrelated worker and task.
3. Promote and claim this AR, create its registered isolated worktree from
   exact current state main, and route all state, Git, test, review, and
   publication mutations through that worktree's `handoffctl run` envelope.
4. Synchronize the complete allowlisted Coordinator snapshot using only
   upstream `tools/vendor.py sync --version v0.7.11`. Do not patch vendored
   files, alter the binding/backend selector, or create a SQLite authority.
5. Mechanically verify source/destination paths, modes, blobs, digests,
   manifest identity, headers, schemas, Git-backend task parsing, generated
   projections, and downstream compatibility. Run relevant bounded formal
   verification with the pinned resource limits.
6. Obtain independent exact-tree review; publish SSH-signed DCO commits and a
   PR; require exact-head CI, merge the reviewed head, and verify the exact
   main post-merge workflows.
7. Write a privacy-safe immutable receipt, record spec acceptance, release the
   AR done, reconcile, and finish with `handoffctl doctor --live` clean.

The upgrade is a release-vendor synchronization, not the unimplemented
`handoffctl upgrade apply` runtime-replacement protocol.

