# AR-1731 plan: wizard agent-picker key contract

1. Reproduce the first-run Agent-step interaction in the installed TUI and in
   renderer/state tests. Establish the exact focused behavior for Space,
   select-all, Enter, search, unavailable rows, and an empty selection.
2. Make the visible hot-key/context help and formal transition model agree:
   Space toggles the focused agent, `a` selects all available agents, and
   Enter continues only after a valid nonempty selection. Empty Enter must
   retain focus and present concise actionable feedback.
3. Keep selection catalog-bound, multi-select, bounded, and compatible with
   search/filtering. Do not infer an agent, silently advance, weaken
   unavailable diagnostics, or introduce a free-form identifier path.
4. Update the formal model/state fixtures and CI coverage so every Agent-step
   keyboard event has a checked outcome, including repeated toggles, empty
   Enter, search results, unavailable options, resize, help overlay, and
   restored drafts.
5. Add a real PTY or equivalent application-runtime regression proving that
   visible selection changes after Space, Enter advances only after selection,
   and the contextual hot-key window matches the rendered route.
6. Run applicable Rust/formal/model/UI gates; require independent exact-head
   review, signed-DCO merge, and exact-main CI before release.
