# AR-1728 plan: rebuild the action-pin update on current main

1. Refresh exact TUI and state remote main, PR #288 head/base/checks/reviews, and
   the immutable old/new upstream action commits. Confirm no worker, claim,
   branch, worktree, or newer PR owns the same workflow line.
2. Claim AR-1728 and create only its declared isolated branch/worktree from the
   exact current TUI main. Route every product/Git/review/publication mutation
   through `handoffctl run`.
3. Apply the single reviewed pin replacement. Reject any unrelated Dependabot
   metadata, merge commit, generated file, workflow behavior change, or mutable
   ref. Inspect the bounded upstream commit range for changed entrypoints,
   permissions, downloads, network behavior, or tool versions relevant here.
4. Run formatting/YAML validation, immutable-action policy, privacy/secret
   scans, dependency/supply-chain checks, Repository Quality, Trusted Main
   fixture coverage, and all other gates selected by the exact diff.
5. Commit with the configured ED25519 SSH key and matching DCO. Push a focused
   replacement PR and record exact head/tree/base identities.
6. Assign a different agent for defect-first review of the complete merge diff
   and upstream action delta. Repair every finding and re-run affected plus full
   gates until the exact reviewed head is green.
7. Merge only the reviewed tree with a signed+DCO local exact-tree merge. Watch
   both exact-main workflows to terminal success and validate the workflow still
   resolves the new immutable pin.
8. Close stale PR #288 as superseded, record a privacy-safe receipt, attach spec
   acceptance, release done, reconcile, and run `doctor --live`.
