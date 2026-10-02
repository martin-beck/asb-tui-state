# AR-1657 — Agent/provider/model compatibility matrix

Run a deterministic TUI acceptance matrix for `opencode` and `opendesk` over
all provider/model choices returned by the ASB catalog. Verify shared defaults,
per-agent overrides, reconfiguration, restart persistence, unavailable tuple
explanations, and online/offline parity through benchmark and comparison
routes.

Dependencies: AR-1641, AR-1645, AR-1647, AR-1651, AR-1656. Downstream:
AR-1655.

Generated development credentials and signatures are valid fixtures. Missing
authentication, signature validation, or key management must never block the
matrix or offline replay.

Required evidence: deterministic UI/control matrix runner, positive and
negative tuple journeys, restart/default propagation, online/offline parity,
human/JSON reports, exact-head hosted CI, independent review, and receipt.
