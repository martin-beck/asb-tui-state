# AR-1725 — operator quickstart parent toolchain propagation repair

Repair the remaining exact-head qualification-runner gap exposed by AR-1575.

## Scope and acceptance

1. In `tools/run-operator-quickstart.py`, resolve the candidate Cargo shim and
   Rustup root from the original sanitized runner environment before replacing
   `HOME` with the disposable qualification root. Forward them to the parent
   ASB router through `ASB_DEV_CARGO` and `ASB_DEV_RUSTUP_HOME`; retain the
   child-facing `ASB_TUI_DEV_RUSTUP_HOME` handoff where required.
2. Treat the runner only as a source of candidate paths. The ASB router must
   continue to perform the authoritative ownership, permission, symlink,
   regular-file, selected-toolchain, descriptor, and substitution checks.
   Missing or hostile candidates must return their existing typed failures
   before TUI execution.
3. Add deterministic focused tests for an isolated `HOME` with a valid
   conventional Rustup shim, an explicit pre-existing ASB override, missing
   Cargo/Rustup inputs, relative and symlinked candidates, wrong ownership or
   write permissions where fixture support permits, and sanitization of
   credential-like environment names. Do not rely only on the worker host.
4. Rerun the actual documented runner with no externally supplied
   `ASB_DEV_CARGO` or `ASB_DEV_RUSTUP_HOME`. It must consume the exact private
   bundle, execute bare `asb tui` through the real nonzero controlling PTY,
   return `development_launched`, and complete the selection-driven setup,
   benchmark, selected/all recording, strict network-denied replay,
   comparison, and analysis journey.
5. Bind the acceptance receipt to exact ASB/TUI commits, trees, executable and
   manifest digests. Record no host paths, environment values, credentials,
   prompts, responses, or raw terminal transcript. Authentication, signing,
   key management, and provider credentials remain visible development-only
   warnings and are never completion gates.
6. Run focused tests and the complete applicable repository gates, obtain a
   different-agent independent review of the exact head/tree, merge only the
   reviewed tree, and verify exact-main post-merge Repository Quality and
   Trusted Main CI before releasing the AR.

This AR owns only the standalone asb-tui qualification runner and its tests.
Any newly proven ASB resolver or product-runtime defect must be recorded in
the ASB project instead of being bypassed here.

