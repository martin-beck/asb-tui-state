# AR-1732 — checkable selections and summary panes

1. Introduce one reusable list/multi-select primitive for agents, providers,
   models, workloads, monitors, measures, and replay/recording choices.
2. Render explicit unchecked and checked markers, a separate focus cursor, and
   unavailable/disabled reasons. Space toggles a focused eligible row; `a`
   select-all / clear-all behavior must be explicitly described per context.
3. Reserve a separately framed pane, or at minimum a stable horizontal-rule
   separation, for the current selection summary. Never mix that summary with
   row description prose.
4. Render selected-item details and current-row descriptions with short
   headings, wrapping, muted secondary text, and typed warning/error styling.
5. Cover single/multi/empty/disabled/long-list/narrow-terminal behavior,
   model transitions, help, ownership, and privacy-safe snapshots.
