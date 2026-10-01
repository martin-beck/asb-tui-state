# AR-1603 — fresh-user wizard-to-offline benchmark acceptance

Run the final disposable, exact-head TUI acceptance for the first-class
journey: install the current default `dev` channel, use the guided wizard to
select agents/providers/authentication/models and shared defaults, launch a
benchmark, record selected workloads, replay with provider egress denied, and
compare results.  Human-readable output is the default; `--json` is explicit.

Dependencies: TUI AR-1600, TUI AR-1601, and ASB AR-1603.  This is an
acceptance gate and must not duplicate cassette or installer implementation.

Required evidence: clean temporary roots, exact paired identities and trees,
wizard selection transcript, benchmark/result artifacts, record/seal/reopen,
offline replay and comparison, typed negative/fault cases, cleanup, independent
review, hosted checks, and post-merge verification.
