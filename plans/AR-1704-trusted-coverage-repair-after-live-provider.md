# AR-1704 — Trusted-main coverage repair after live-provider integration

Repair the exact-main Trusted verification failure introduced after the live
provider integration. The observed total line coverage was 89.97%, below the
existing 90% threshold. Add behavior-relevant tests for the newly merged
provider/setup and command-boundary paths (including explicit live mode and
typed no-credential failure), without weakening thresholds or excluding source.

Acceptance requires local full-suite and coverage evidence, independent review,
signed/DCO hosted PR checks, and green exact-main Repository Quality and Trusted
main verification for the resulting merge commit. Development-only missing
credentials remain warning/non-blocking during setup; this repair must not add
an authenticated-router or production-key requirement.
