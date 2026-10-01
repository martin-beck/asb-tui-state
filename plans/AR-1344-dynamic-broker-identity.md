# AR-1344 — asb-tui dynamic development broker identity

## Scope

Make the development broker descriptor validate the exact current ASB and
asb-tui identities after either repository advances.

## Acceptance

- Descriptor identity comes from the bounded development handoff/build input,
  not stale compile-time pre-merge literals.
- Current exact ASB/asb-tui heads validate successfully.
- Stale, malformed, unknown, and mismatched identities fail closed with typed
  development diagnostics.
- Stable/non-development broker behavior is unchanged.
- Hosted checks and exact-head cross-project fixture tests pass.

## Boundaries

Development/mock prototype only. Missing authentication, signatures, and key
management must never block this path.
