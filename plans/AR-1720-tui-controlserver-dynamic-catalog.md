# AR-1720 — TUI ControlServer dynamic provider-catalog bridge

Implement the TUI side of the additive ASB ControlServer v1.15 dynamic
provider-catalog contract. The route must request the selected provider's
catalog, negotiate the common version, validate provider profile, generation,
digest, capabilities, and model availability, and project every eligible
OpenRouter explicit `:free` and free-router model into wizard selection.

Scope includes:

- request/response codec and v1.15 capability negotiation with typed older-
  server and unavailable responses;
- refresh lifecycle, stale-generation/digest rejection, provider-profile
  binding, and renderer-neutral wizard projection;
- human and `--json` diagnostics for missing auth, quota, stale catalog,
  model mismatch, and unavailable provider outcomes;
- installed `asb tui install` → bare `asb tui` paired qualification against
  the exact ASB AR-1719 head;
- deterministic catalog fixtures, privacy checks, PTY/formal/help inventory
  coverage, independent review, signed/DCO product PRs, and hosted checks.

Development mode may display authentication, signature, and key-management
warnings without blocking setup. Explicit live requests must remain distinct
from local/mock and offline replay and must never silently substitute a static
catalog or fallback provider.

Dependency: ASB AR-1719 provides the normalized dynamic catalog, typed
availability/model-mismatch contract, deterministic fixtures, and privacy-safe
receipt fields. It is merged at ASB commit `6bd9b836` with hosted evidence.
This external dependency is not represented as a local task edge. AR-1713 is
the later consumer of this bridge for installed live-run, capture, replay, and
comparison qualification; that acceptance gate remains required and is not
silently waived.
