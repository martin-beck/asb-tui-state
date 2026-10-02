# AR-1664 — Trusted-main channel-selection coverage repair

## Scope

Investigate trusted-main workflow run `37002888017` for exact source head
`fa6483f`, reproduce its coverage qualification failure in a detached isolated
worktree, and repair the underlying behavior coverage for the AR-1658 channel
selector. Keep repository coverage thresholds unchanged and preserve the
development-only nonblocking authentication, signature, and key-management
contract.

## Acceptance

- The failure is reproduced or explained from the hosted run's authoritative
  logs and exact head.
- Focused tests exercise observable channel-selection behavior, including the
  default path, explicit changes, persistence/restart, unavailable choices,
  diagnostics, and human/JSON output as implemented.
- Existing coverage thresholds and qualification gates are unchanged.
- Local focused and repository-required checks pass at the repair head.
- The repair is independently reviewable, SSH-signed, DCO-attested, and pushed
  as a PR with exact-head evidence.

## Dependencies and boundaries

AR-1661 supplies the repaired coordinator graph and AR-1658 supplies the
channel-selector behavior contract. This task changes only product tests/code
needed to cover the behavior exposed by the trusted-main failure; it does not
turn development credential or authenticity warnings into blocking gates.
