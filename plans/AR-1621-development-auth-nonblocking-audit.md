# AR-1621 — development authentication and provenance non-blocking audit

Audit every TUI wizard, provider/model selection, API-key, install, recording,
replay, and analysis path. Missing authentication, signatures, or key
management must show an explicit `development-only` warning and use generated
local fixture identity rather than blocking the prototype. Preserve
fail-closed hooks for future production mode and prove the behavior across the
ASB control boundary.

Required evidence: path inventory, missing-credential negative tests, visible
warning and fixture receipts, production-boundary tests, independent review,
hosted checks, and exact-main verification.
