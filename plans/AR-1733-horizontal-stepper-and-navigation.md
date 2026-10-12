# AR-1733 — horizontal stepper and navigation

1. Define a formal step sequence for landing, agent, provider, credential
reference, model, workload, monitor/measure, plan review, execution, results,
comparison, and configuration re-entry where applicable.
2. Render a horizontal top stepper with a strong current-step highlight,
complete marker, future marker, and unavailable reason; collapse safely to a
compact progress representation when the terminal is too narrow.
3. Standardize keys: arrows or `j`/`k` move focus, Space toggles, Enter
continues a valid step, Backspace/Left returns, Tab cycles panes, Esc cancels
or backs out only where modeled, and `?`/`h` opens contextual help.
4. Ensure navigation cannot bypass validation, erase an uncommitted draft
silently, or imply completion before authoritative effects succeed.
5. Add transition, resize, PTY, model, help, ownership, and key-conflict tests.
