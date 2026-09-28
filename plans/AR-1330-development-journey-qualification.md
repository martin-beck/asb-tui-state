# AR-1330 — Development credential journey qualification

Qualify a disposable, credential-free development journey through the standalone
development route (paired with ASB AR-1496, AR-1443 and the completed AR-1500)
from clean TUI install through
enrollment, provider/model selection, agent defaults, mock capture, strict
offline replay and comparison. The journey must continue when authentication,
signature validation, or key management is absent, showing warnings instead of
blocking. Record exact ASB/asb-tui revisions and label every result as
development/mock evidence.

This is the prototype release gate; it does not prove production authentication,
secret storage or external-provider reachability.
