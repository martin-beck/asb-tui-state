# AR-1614 — immutable development-channel bundle and installability

Publish and qualify the exact TUI bundle consumed by ASB's default `dev`
channel. A clean machine must be able to install and launch the current TUI
without a pre-existing checkout, while upgrade, rollback, removal, and
unavailable-channel diagnostics preserve configuration and explain the next
action.

Generated development identities and visible development-only warnings are
allowed. Missing production authentication, signatures, or key-management
services must never block this prototype path; production publication remains
fail-closed on invalid or mismatched immutable evidence.

Required evidence: exact immutable manifest/digest, clean-machine install and
launch, current-head/version handoff, upgrade/rollback/remove negatives,
credential-free output, independent review, hosted checks, and exact-main
post-merge verification paired with ASB.
