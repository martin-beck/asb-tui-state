# AR-1738 plan: wizard catalog viewport and availability presentation

1. Read the asb-tui and coordinator development documentation, claim an
   isolated worktree from exact current main, and reproduce the defect with a
   deterministic catalog containing more than eight agent rows.
2. Replace the fixed prefix rendering with a bounded scrolling viewport. The
   focused row must always be rendered after Up/Down, filtering, resize, and
   catalog-kind changes; selection and search semantics must remain intact.
3. Remove formal element identifiers from human-facing wizard cards and use
   short, localized human labels such as `Step: Agent`.
4. Carry the typed agent availability reason through the catalog adapter and
   render concise actionable text for unavailable rows. Preserve a distinct
   all-unavailable explanation without claiming that an agent is selectable.
5. Update the formal UI model and generated model artifact for the viewport
   and availability contract; add focused render/state tests including a
   catalog larger than the viewport, filtering, and each unavailable reason.
6. Run formatting, focused and workspace checks, model/parity/accessibility
   gates, an installed or PTY presentation journey where applicable, and
   obtain independent exact-head review. Push signed-DCO commits, merge only
   after required CI succeeds, and record post-merge exact-main evidence.

Done requires that a user can always see the focused option, never sees a raw
`wizard.*` identifier, and receives the catalog's truthful availability reason
without any ASB protocol or catalog-validation weakening.
