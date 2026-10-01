# AR-1617 — explicit cassette seal, reopen, and removal operations

Expose the missing typed cassette lifecycle actions in the TUI and ASB
control route: explicit seal/finalization, reopen/resume only from interrupted
reconciliation, and bounded removal of selected development artifacts. Bind
every action to cassette, campaign, generation, provider, agent, and workload
identity, rejecting terminal, stale, or mismatched requests without mutation.

Generated development identities and missing production authentication,
signatures, or key management remain warning-only. Production deletion stays
fail-closed and explicitly authorized.

Required evidence: versioned wire schema, selectable TUI actions, positive
interrupted-capture/reconcile/seal path, terminal/stale/remove negatives,
offline replay compatibility, independent review, hosted checks, and exact
main verification paired with ASB.
