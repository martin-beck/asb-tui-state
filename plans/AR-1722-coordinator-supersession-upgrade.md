# AR-1722 — coordinator supersession-chain vendor upgrade

1. Acquire exact upstream Agent Workflow Coordinator v0.3.14 in an isolated,
   clean checkout and verify its tag/commit identity.
2. Use the upstream `tools/vendor.py sync` command to upgrade the complete
   vendored file set; never patch a vendored file directly.
3. Review the entire vendor diff and verify `coordinator.binding.json`,
   `coordinator.backend.json`, and project profile remain unchanged.
4. Run upstream/vendor integrity, headers, the complete coordinator unit suite,
   formal checks, render-status, privacy checks, and live doctor.
5. Add focused downstream integration coverage for valid and invalid
   `superseded_by` chains if the upstream suite does not exercise the TUI
   project profile directly.
6. Record `superseded_by: AR-1668` on AR-1672 only after the upgraded schema is
   authoritative, then prove AR-1673 promotion admission succeeds while every
   malformed or unfinished chain still fails closed.
7. Obtain independent review, commit with SSH signature and DCO, reconcile,
   snapshot, and verify live state before releasing the AR.

This is coordination tooling and metadata work only. It must not modify the
asb-tui or ASB product repositories.
