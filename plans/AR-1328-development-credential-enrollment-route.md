# AR-1328 — Development credential-enrollment route

## Outcome

Add a selectable TUI route for the development credential contract (paired with
ASB AR-1499 and AR-1500): choose a
provider and authentication method, generate or enter a development fixture
credential, test it, rotate/reset it, and see bounded status without displaying
production secrets.

## Scope

- Render generated development credentials and signatures as explicitly
  development-only; never claim keychain or production secrecy.
- Bind enroll/test/rotate/reset/status to ASB AR-1499 and AR-1500 with
  generation, cancellation and restart fencing.
- Add contextual help, typed validation, failure/retry choices and deterministic
  mock-provider tests.

Production keychain, remote trust and secure authentication are deferred to
ASB AR-1501 and TUI AR-1331.
