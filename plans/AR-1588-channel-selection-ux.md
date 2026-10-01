# AR-1588 — asb-tui channel selection UX

Bind the standalone TUI's install/status/launch/reconfigure screens to the
explicit ASB release-channel field. A fresh development setup defaults to
`dev`, presents the selected channel and current-main source identity, keeps
an existing installation's channel unchanged unless the user explicitly
selects another, and explains unavailable stable/nightly/experimental
channels without blocking development setup.

Keep this renderer/UI scope separate from the ASB backend bridge. Development
fixtures may use generated identity/signature material; missing
authentication, signature validation, and key management must remain visible
warnings rather than blockers. Production/stable behavior remains fail-closed.

Acceptance requires keyboard/TUI and renderer-neutral tests, JSON/status
projection parity, cancellation/retry behavior, and exact-head hosted review.
