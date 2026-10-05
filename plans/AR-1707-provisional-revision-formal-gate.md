# AR-1707 provisional revision and formal UI gate requalification

## Scope

At the exact current asb-tui main head, define and implement the revision
lifecycle used by selection-driven wizard state and cross-process handoff:

- `provisional`: locally edited but not committed/published;
- `committed`: atomically persisted and bound to the current catalog/channel
  generation;
- `stale`: based on an older catalog, channel, provider/model, or source
  revision and rejected before launch/capture;
- `superseded`: replaced by a newer committed revision and never silently
  revived;
- `unavailable`: missing provider/model/channel evidence with a typed
  diagnostic rather than an implicit fallback.

Bind these outcomes to the executable UI state model and source inventory.
Rerun the formal model validator, source-parity checker, transition/property
tests, and protected hosted formal gate after the wizard/live-provider changes.

## Acceptance

- Positive and negative tests cover edit/cancel, commit/restart, stale
  catalog/provider/model revisions, supersession, unavailable selections,
  capture/replay handoff, and typed human/JSON diagnostics.
- Model-to-source and source-to-model parity remains exact; no UI route or
  transition is omitted from the formal inventory.
- The formal journey includes the supported top-level command boundary:
  `asb tui install` materializes the tested bundle and a subsequent bare
  `asb tui` reaches the same modeled wizard/launch states. Direct invocation
  of an internal TUI binary cannot satisfy this gate.
- Current-head receipt records source/model revisions, exact test commands,
  and hosted gate identities without secrets or private paths.

The development prototype may continue with generated authenticity metadata
and absent credentials; these are warnings, never hidden prerequisites.
