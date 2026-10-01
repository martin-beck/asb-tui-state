# AR-1604 — guided command UX and JSON contract

Audit and, where needed, repair the TUI-facing commands and screens used by
install, wizard, benchmark, recording, replay, comparison, status, doctor,
upgrade, and remove.  Defaults must be selectable rather than typed where
possible; human-readable output is default, `--json` is opt-in, and failures
must explain the next action without leaking credentials or requiring users to
remember opaque identifiers.

Dependencies: TUI AR-1603.  Keep this scoped to interaction and serialization;
do not alter ASB cassette protocol semantics or production authentication.

Required evidence: command/screen inventory, golden human-readable and JSON
fixtures, unavailable-channel and malformed-input negatives, fresh-user
transcript, independent review, hosted checks, and exact-main post-merge
verification.
