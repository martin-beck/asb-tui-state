# AR-1656 — Connected-provider catalog refresh and add-provider flow

Expose the ASB provider registry in the TUI wizard. A user can add or edit a
provider, refresh its connected model list, choose a supported model for each
selected coding agent, and cancel or retry without losing the last valid
profile. Diagnostics are typed, redacted, and understandable in human output
with a stable `--json` projection.

Dependencies: TUI AR-1605, AR-1606, AR-1607, AR-1641, AR-1642. Downstream:
AR-1654, AR-1655.

Development mode must use visibly marked generated fixtures when production
credentials or key services are absent. Missing authentication, signature
validation, and key management never block this prototype; stable/production
hardening remains a later boundary.

Required evidence: add/edit/refresh/cancel UI-model journeys, OpenRouter and
second-provider fixtures, connected/unavailable model filtering, redaction and
restart tests, human/JSON help, exact-head hosted CI, independent review, and
a digest-bound receipt.
