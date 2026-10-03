# AR-1695 — Fan-out RunRequest wire-contract conformance

## Scope

Close the paired ASB/TUI integration seam for selected-agent/workload fan-out.
The TUI must serialize the complete versioned ASB `run_request` object and
validate it against the ASB control contract before dispatch.

## Acceptance

- Required identity, provenance, mode, cassette/credential-reference, and bounded
  limit fields are present in human and JSON paths.
- The serialized request validates against the ASB control schema and is accepted
  by the real control route for local/mock development execution.
- Missing development authentication, signatures, or key-management metadata is
  visible as a warning only; it cannot block request validation or offline replay.
- Negative tests cover missing fields, mismatched digests/revisions, invalid
  limits, duplicate idempotency keys, and unavailable provider/model choices.
- Evidence records exact ASB and TUI heads and the fixture/request digest.
