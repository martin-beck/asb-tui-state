# AR-1604 — guided command UX and JSON contract

Audit and, where needed, repair the TUI-facing commands and screens used by
install, wizard, benchmark, recording, replay, comparison, status, doctor,
upgrade, and remove.  Defaults must be selectable rather than typed where
possible.  Build a command/screen matrix naming the owning binary, human-
readable default, machine-readable selector (`--json` or existing
`--format json`), exit class, typed envelope, and compatibility alias.  Failures
must explain the next action without leaking credentials or requiring users to
remember opaque identifiers; unavailable-channel behavior must remain scoped to
the lifecycle owner rather than treated as a generic ASB error.

Dependencies: TUI AR-1603.  Keep this scoped to interaction and serialization;
do not alter ASB cassette protocol semantics or production authentication.

Required evidence: command/screen matrix, golden human-readable and
machine-readable fixtures, unavailable-channel and unknown/malformed-input
negatives, credential-free output, fresh-user transcript, independent review,
hosted checks, and exact-main post-merge verification.
