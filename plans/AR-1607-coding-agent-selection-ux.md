# AR-1607 — Coding-agent selection and compatibility UX

Extend the TUI wizard with selection-driven coding-agent entries for
`opencode`, `opendesk`, and future adapters. Render the provider/model/auth
choices allowed by the selected adapter, explain unavailable tuples without
requiring model-ID typing, and preserve the last valid selection on cancel or
failed validation. The same adapter identifiers must flow into benchmark,
recording, offline replay, and comparison routes.

Dependencies: TUI AR-1605 and ASB AR-1609. Downstream: TUI AR-1606 and
TUI AR-1603.

Development mode must remain usable without real credentials, signatures, or
key-management services; show development-only warnings rather than blocking.

Required evidence: renderer/formal model updates, opencode/opendesk fixtures,
selection and unavailable-tuple tests, cancellation/restart coverage,
human-readable help plus stable `--json`, exact-head hosted CI, independent
review, and a digest-bound receipt.
