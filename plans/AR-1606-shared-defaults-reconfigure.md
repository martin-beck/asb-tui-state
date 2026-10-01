# AR-1606 — shared defaults and reconfiguration

Extend the TUI wizard beyond first launch: edit an existing provider/model/auth
entry, add a provider, apply a selected configuration to all or selected
agents, and save it as the default for the next run. Show a bounded summary of
the effective configuration and preserve the previous valid state on failure.

Dependencies: TUI AR-1605, ASB AR-1608. Downstream: AR-1603 and AR-1604.

Development-only generated identity material and missing security services are
visible warnings, never blockers. Secrets remain environment-backed and are
never rendered, persisted, or included in evidence.

Required evidence: formal model/help coverage, restart persistence, multi-agent
propagation, add-provider and rollback negatives, exact-head CI, review, and
receipt.
