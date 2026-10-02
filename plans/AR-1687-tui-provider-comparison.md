# AR-1687 — TUI provider-bound comparison qualification

Exercise the TUI comparison route against ASB’s provider-bound comparison
contract for available, unavailable, asymmetric, and multi-candidate runs.
Verify that human output remains understandable and structured output remains
privacy-safe and typed.

## Acceptance

- TUI displays unavailable baseline/candidate sides and does not claim
  comparability.
- Provider/model and execution-binding differences remain visible as
  confounders.
- Multi-candidate per-pair results and aggregate availability are preserved.
- No credential, live provider, signature service, or key manager is required.
- Exact-head receipt, hosted checks, independent review, and no-secret scan
  pass.
