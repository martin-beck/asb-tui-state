# AR-1706 — Current-main PTY/control repair qualification

Qualify and, if necessary, coordinate the focused repair for the current-main
installed TUI PTY/control path. The receipt must begin at the supported
installed entrypoint (`asb tui install`, then bare `asb tui`) and prove the
controlling PTY, ASB control handshake, live-mode handoff, bounded progress,
cancellation/quit, restart, and cleanup at exact paired heads. This AR owns
state and qualification only; any source repair belongs in the product PR
selected by the coordinator.

Current product heads observed for this AR are asb-tui `68d9a787b6673f13773151e1d8cbbc1a032be7bb`
and ASB `401253e53160dc51b39b6618c2b2459cba569c7f`. Re-fetch both before
promotion or claiming evidence. Pair with ASB AR-1702 (credential-backed live
OpenRouter qualification) and ASB AR-1703 (paired live-admission/control
contract, if that task is the applicable current identifier); these are
cross-repository references in prose, not local dependency IDs.

The matrix must preserve the development policy: missing authentication,
signatures, and key management are warning-only during setup; an explicit live
run with no credential or a provider/control failure is a typed actionable
failure; and live mode never silently falls back to local/mock or replay.
Local/mock remains an explicit labelled alternative. Production/release claims
remain out of scope.

Acceptance:

1. Exact-head installed PTY/control evidence proves the top-level commands
   reach the installed TUI and ASB control route, with no direct-binary-only
   shortcut.
2. Live mode, provider/model identity, bounded progress, typed failure,
   cancellation/quit, restart, and cleanup are visible and truthful.
3. Credential-free setup is warning-only; credential-free live and bounded
   provider/control failures are typed; explicit local/mock is separately
   identified and never used as live evidence.
4. Receipt records exact refreshed ASB/TUI heads, installed executable
   digests, command/result digests, and no secrets, prompts, raw responses, or
   production-readiness claim.
