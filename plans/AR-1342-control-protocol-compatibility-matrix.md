# AR-1342 — ASB control protocol compatibility matrix

## Scope

Define a machine-checkable compatibility matrix for the ASB control and TUI
development-channel envelopes, including supported minors, operation names,
schema versions, and exact source identities.

## Acceptance

- Matrix fixtures cover supported and rejected protocol minors and operations.
- Current exact ASB/asb-tui heads pass the matrix in development mode.
- Stale, malformed, or production-only envelopes fail closed with named errors.
- Fixtures contain no credentials or private transcripts and are labeled
  `development-only`.

## Boundaries

No production authentication, key management, or stable-release support is
introduced by this AR.

