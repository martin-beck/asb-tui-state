# AR-1328 — Development credential-enrollment route

## Outcome

Add a selectable TUI route for the development credential contract (paired with
ASB AR-1499 and AR-1500): choose a provider and authentication method, have the
wizard automatically generate a local development fixture credential, test it,
rotate/reset it, and see bounded status without displaying production secrets.

## Scope

- Render generated development credentials and signatures as explicitly
  development-only; never claim keychain or production secrecy.
- If authentication, signature validation, or key management is unavailable,
  continue with the local fixture and show a non-blocking development warning.
- Bind enroll/test/rotate/reset/status to ASB AR-1499 and AR-1500 with
  generation, cancellation and restart fencing.
- Add contextual help, typed validation, failure/retry choices and deterministic
  mock-provider tests.

Production keychain, remote trust and secure authentication are deferred to
ASB AR-1501 and TUI AR-1331.
