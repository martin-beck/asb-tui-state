# AR-1603 — fresh-user wizard-to-offline benchmark acceptance

Run the final disposable, exact-pair TUI acceptance for the first-class
journey: install the current default `dev` channel, use the TUI-owned guided
wizard to select agents/providers/authentication/models and shared defaults,
invoke the ASB setup/control boundary, launch a benchmark, and use the
authenticated AR-1605 cassette authority to record, seal, reopen, replay with
provider egress denied, and compare results.  Pin and record both repository
heads/trees; a CLI file replay without the authority handoff is insufficient.
Human-readable output is the default.  The evidence must identify whether each
route uses `--json` or the existing `--format json` selector.

Dependencies: TUI AR-1600, TUI AR-1601, and ASB AR-1603.  This is an
acceptance gate and must not duplicate cassette or installer implementation.

Required evidence: clean temporary roots, exact paired identities and trees,
wizard selection transcript, ASB authority handoff, benchmark/result artifacts,
record/seal/reopen, offline replay and comparison, typed negative/fault and
unknown/malformed argument cases, credential-free output, cleanup, independent
review, hosted checks, and post-merge verification.
