# AR-1581 complete bootstrap and control coverage

Exercise the real startup/control request set against the current ASB backend:
benchmark and measurement catalogs, history, agents, providers, configuration,
recording, authentication status, validation, apply, start/cancel/completion,
and typed malformed/stale failures. Development fixtures may use generated
local credentials, but must never block on production authentication,
signatures, or key management.
