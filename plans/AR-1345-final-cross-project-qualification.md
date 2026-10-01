# AR-1345 — ASB/asb-tui exact-head final qualification

## Scope

Qualify the complete setup and development broker journey using detached clean
worktrees of current ASB and asb-tui main heads.

## Acceptance

- Exact ASB/asb-tui commit and tree identities are recorded.
- Fresh dev install/materialization, status/doctor, and removal are typed and
  credential-free.
- Dynamic descriptor reaches `run --broker --development` and returns a valid
  bounded lifecycle result.
- Stale, malformed, unsupported, and missing identity cases fail closed.
- Offline/no-credential development behavior remains usable and non-blocking.
- Evidence is published and independently reviewed.

## Boundaries

Development/mock qualification only; no production authentication, signature,
or key-management gate may block the prototype.
