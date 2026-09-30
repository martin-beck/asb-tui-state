# AR-1343 — asb-tui development broker entrypoint

## Scope

Provide the descriptor-bound development broker entrypoint consumed by ASB's
dev lifecycle launch path.

## Acceptance

- `run --broker` accepts the closed development descriptor and dispatches the
  requested lifecycle operation.
- Source identities, protocol minor, schema, and development-only classification
  are validated fail-closed.
- Exact-head cross-project fixtures pass without credentials or production keys.

## Boundaries

Development/mock only; production authentication and secret-management remain
future hardening work and must not block the prototype.

