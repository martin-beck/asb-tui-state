# AR-1685 TUI state spec-acceptance metadata

## Scope

Add a supported `handoffctl accept` mutation/API to the TUI coordinator state
repository. Validate active ownership, task revision, task spec reference and
revision, known evidence class, evidence reference, SHA-256 digest, and pass
status before recording the acceptance receipt used by `release --status done`.

## Acceptance

- Valid acceptance records the complete typed receipt atomically.
- Invalid, stale, mismatched, unowned, or malformed requests fail closed and
  leave task metadata unchanged.
- Existing lifecycle and generated projections remain compatible.
- Vendor manifest and focused/full coverage checks pass at the unchanged gate.
- Development-only missing authentication, signatures, and key management are
  warnings, never blockers.
