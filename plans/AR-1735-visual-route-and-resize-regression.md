# AR-1735 — visual route and resize qualification

1. Build deterministic renderer fixtures for landing, all wizard steps,
configuration/re-entry, live progress, reports/comparison, errors, warnings,
empty lists, unavailable entries, and help overlay.
2. Exercise wide, ordinary, narrow, and minimum-supported terminal dimensions;
resize during selection/help/draft state and prove focus, selections, and
footer context remain valid.
3. Run color, monochrome, and limited-Unicode fixtures: selection/focus/current
step meaning must survive without color and with supported ASCII fallback.
4. Enforce UI_OWNERS, source modules, formal model, help catalog, keybindings,
and snapshots as one CI parity surface; malformed/absent visual metadata fails.
5. Add keyboard-only PTY regression journeys and bounded screenshot/text-grid
goldens reviewed for legibility and privacy.
