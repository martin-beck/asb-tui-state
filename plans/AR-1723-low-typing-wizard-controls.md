# AR-1723 — bounded low-typing wizard controls

Implement the usability repair demonstrated by AR-1597 without changing ASB
product code or weakening the exact provider/catalog contracts already
qualified by AR-1668 and AR-1720.

## Scope

1. Replace the supported wizard's free-form configuration/default field with a
   bounded preset or structured selector whose selected value maps exactly to
   the existing typed control request.
2. Offer safe credential-reference choices, including the conventional
   `OPENROUTER_API_KEY` environment reference, without reading, rendering, or
   persisting any credential value. Optional custom reference editing must be
   explicitly advanced and validated before effects.
3. Replace recording-mode and replay-policy text entry with bounded enum-backed
   selection controls. Invalid, stale, unavailable, and cross-mode choices must
   fail before materialization or dispatch and may never trigger silent
   fallback.
4. Preserve catalog-backed agent, provider, and model selection, restart and
   cancellation semantics, exact revision/digest fencing, and the default-dev
   warning-only authentication boundary.
5. Update the executable TUI state/window/transition model, source inventory,
   UI ownership declarations, contextual help catalog, and coverage gate for
   every added or changed element and action. Every control must have meaningful
   context-specific help and keyboard guidance.
6. Add an authoritative renderer-route regression using the same real wizard
   state transitions as AR-1597. The supported happy path must complete with
   zero free-form characters and at most 24 total key events from wizard entry
   through the committed benchmark/record/replay selection. The test must
   report categorized action counts and fail if a future change exceeds either
   bound.

## Acceptance and qualification

- Focused state, renderer, navigation, help, ownership, formal-model, codec,
  persistence, cancellation, stale-selection, and privacy tests pass.
- The full locked workspace gates pass without excluding existing tests,
  lowering thresholds, or mutating the dirty shared product checkout.
- A disposable exact-head journey proves setup, benchmark selection, recording,
  strict offline replay, comparison handoff, restart, and cancellation without
  documentation lookup or free-form input on the supported path.
- Human and JSON diagnostics remain stable, actionable, and free of credential
  values, provider payloads, private paths, and prompts.
- Independent exact-head review, required hosted checks, signed+DCO merge, and
  exact-main post-merge checks pass before AR-1723 is done and AR-1597 resumes.

This AR owns only the standalone `asb-tui` implementation, tests, model, help,
and documentation. Any newly discovered ASB protocol gap must be recorded as a
separate paired ASB AR rather than implemented in the ASB repository here.
