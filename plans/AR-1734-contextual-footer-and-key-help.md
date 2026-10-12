# AR-1734 — contextual footer and hotkey help

1. Bind the focused/hovered element and active route to the existing help
catalog through stable IDs; never derive help from untrusted displayed text.
2. Render a persistent concise footer with current action hints and one useful
description; reserve `?`/`h` for a larger context-filtered hotkey/help overlay.
3. The overlay lists only currently legal actions, grouped by navigation,
selection, editing, lifecycle, and help; it must preserve the underlying draft
and restore focus on close.
4. Give disabled/unavailable items actionable explanation and remediation in
the footer/overlay without exposing credentials, prompts, private paths, or
provider payloads.
5. Add completeness, focus-change, overlay, key-collision, narrow-terminal,
formal model, UI ownership, and CI drift tests for every visible action.
