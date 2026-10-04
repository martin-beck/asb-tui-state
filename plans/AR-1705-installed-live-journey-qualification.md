# AR-1705 — Installed TUI live OpenRouter journey qualification

Run the complete clean-room development journey from the supported installed
entrypoint: install the default `dev` channel with `asb tui install`, launch
`asb tui`, complete the provider/model/API-key reference setup, and explicitly
start a credential-backed live OpenRouter benchmark. Prove that the installed
handoff preserves live mode and configuration, displays bounded progress and
provider/model identity, and reports the real online outcome.

The journey must also run credential-free and with a bounded provider failure.
Missing development credentials and authenticity/key-management status are
warning-only during setup; an explicitly requested live run must terminate in
a typed actionable failure and must never silently become local/mock or replay.
The local/mock path is tested separately and visibly labelled. Restart and
cleanup must leave no secret or raw provider response in durable state.

Pair with ASB AR-1702, which owns the provider-facing credential-backed smoke
and negative matrix. This AR owns the installed TUI journey and receipt; use
the exact paired ASB/TUI heads and do not treat a direct development-binary
test as installed-entrypoint evidence.

Acceptance:

1. A clean-room install and top-level launch reach the wizard and live run
   without invoking an internal binary directly.
2. With an operator-supplied credential, the installed TUI completes one
   bounded real OpenRouter request (or records a typed provider failure), with
   explicit Online mode and no mock/replay substitution.
3. Credential-free setup remains usable with a warning; credential-free live
   execution is a typed failure. Explicit local/mock remains separately
   selectable and labelled.
4. The receipt includes exact ASB/TUI heads, installed executable digests,
   redacted mode/provider/model/outcome evidence, restart/cleanup results, and
   no secrets, prompts, or raw responses.
