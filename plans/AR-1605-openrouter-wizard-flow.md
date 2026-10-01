# AR-1605 — OpenRouter setup wizard flow

Add a selection-driven TUI flow for OpenRouter provider, authentication
method/API-key reference, connected supported-model choices, and per-agent
selection. Surface connectivity and development-only warnings without
requiring users to type model IDs or copy secrets into files.

Dependencies: TUI AR-1594, ASB AR-1607. Downstream: AR-1603.

Missing authentication, signatures, and key-management services must never
block development mode. The TUI must redact secrets, offer cancellation and
retry, and preserve the last valid configuration on failed saves.

Required evidence: formal state/help updates, real control-server journey,
OpenRouter model fixtures, unavailable-model and cancellation negatives,
exact-head hosted CI, independent review, and receipt.
