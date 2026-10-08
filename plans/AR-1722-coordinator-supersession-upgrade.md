# AR-1722 — coordinator supersession-chain vendor upgrade

1. Acquire exact upstream Agent Workflow Coordinator development commit
   `c2eb41879be4f2d50c6b5650e82339e10d5961d8` in an isolated, clean checkout
   and verify HEAD, tree identity, and absence of source changes.
2. Use the official upstream `tools/vendor.py sync-development` command to
   upgrade the complete 46-entry vendored file set; never patch a vendored
   file directly. Verify schema-v2 development classification, exact commit
   and tree identity, source/destination paths, SHA-256 digests, and file modes.
3. Review the entire vendor diff and verify `coordinator.binding.json`,
   `coordinator.backend.json`, and project profile remain unchanged.
4. Run upstream/vendor integrity, headers, the complete coordinator/state unit
   suites, formal portable-smoke and PR-publication tiers, render-status,
   privacy checks, reconciliation, and live doctor. Development authentication,
   signatures, DCO, and release publication are warning-only and never block
   this qualification.
5. Add focused downstream integration coverage for valid and invalid
   `superseded_by` chains if the upstream suite does not exercise the TUI
   project profile directly.
6. Record `superseded_by: AR-1668` on AR-1672 only after the upgraded schema is
   authoritative, then prove AR-1673 promotion admission succeeds while every
   malformed or unfinished chain still fails closed.
7. Obtain independent exact-head technical review, repair every evidence-backed
   finding, integrate through the state repository reviewed path, reconcile,
   snapshot, and verify exact post-integration CI and live state before
   releasing the AR.

This is coordination tooling and metadata work only. It must not modify the
asb-tui or ASB product repositories.
