# AR-1730 plan: Coordinator v0.4.0 release vendor and TUI-state compatibility

## Scope

Adopt the exact upstream Agent Workflow Coordinator `v0.4.0` release into the
ASB-TUI coordination state repository. The upstream tag resolves to commit
`712b36ea3d188237cbe8104e70d905094f93a96b` and tree
`c496306050a805111f89b3f7bc4cfb0910f27535`. The release tag is lightweight;
record that fact explicitly and rely on the verified commit/tree and official
vendor synchronizer rather than claiming an annotated tag signature.

The state repository currently vendors development Coordinator commit
`e863b57edc7f7a21b2aff2c7b45ce226e12637d2` and tree
`eee603591b917eeca244425559d7c67bb88a7268`. Synchronize the complete
allowlisted file set through the release `vendor.py sync` path from a clean
exact-tag source checkout. Never patch a vendored byte or alter the project
binding, Git backend, profile, privacy policy, or task intent.

## Required work

1. Refresh and independently verify upstream refs, exact commit/tree, commit
   ancestry, declared Coordinator version, source cleanliness, and tag object
   type. Record the lightweight-tag limitation and do not overstate release
   provenance.
2. Repair the stale missing product-worktree registration through the supported
   coordinator-wrapped Git maintenance path before claiming this task. Preserve
   every live worker, dirty path, branch, and unrelated repository.
3. Claim this AR and create its registered isolated state worktree from exact
   state main. Run all product, state, Git, test, review, and publication
   mutations through `tools/handoffctl run` under the claim.
4. Synchronize the complete Coordinator vendor set using the official release
   path, mechanically verify every source/destination, blob, mode, digest,
   manifest field, version, and deterministic manifest identity, and review the
   full vendor diff. Add only ASB-TUI-owned compatibility or fixture coverage
   required by the new Coordinator behavior, with positive and negative tests.
5. Run vendor verification, source headers, all state tests, generated-view and
   privacy checks, applicable formal models, TUI compatibility gates, focused
   and full applicable product tests, reconciliation, snapshot, and live doctor.
6. Obtain independent exact-tree review, publish an SSH-signed DCO commit and
   PR, wait for every required exact-head check, and merge only the reviewed
   tree through the documented signed merge path. Verify exact-main workflows
   after merge.
7. Create a privacy-safe receipt binding upstream commit/tree, vendor manifest,
   compatibility evidence, review, CI, merge, and post-merge verification.
   Record spec acceptance, release this AR done, reconcile, and finish with a
   successful live doctor. A future Coordinator release or upstream tag-signing
   repair requires a separate AR.

## Boundaries

This AR is limited to ASB-TUI coordination state and its Coordinator consumer
compatibility. Do not modify `agent-systems-benchmark`, its state repository,
the standalone product outside its compatibility contract, or unrelated ARs.
Do not weaken signatures, DCO, privacy, provenance, thresholds, or fail-closed
gates. Development and source-only product release status remains distinct from
Coordinator vendor qualification.
