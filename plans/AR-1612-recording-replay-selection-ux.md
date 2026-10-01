# AR-1612 — recording and offline replay selection UX

Add a concise TUI action flow for selecting one, several, or all implemented
workloads and agents, starting a bounded recording campaign, sealing the
result, activating it for offline replay, and opening comparison results. Keep
selection transactional, preserve previous defaults on cancellation/failure,
and show redacted credential references only. Support the same flow in the
human-readable and opt-in JSON event projections.
