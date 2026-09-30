---
{
  "branch": "feature/ar-1335-configuration-materialization",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T13:45:03+00:00",
  "depends_on": [
    "AR-1333",
    "AR-1334"
  ],
  "id": "AR-1335",
  "next_action": "Await exact-head CI/review for cae7055; then merge AR-1335 and promote AR-1336 if AR-1323 is done.",
  "owner": "tui-ar1335-dev-20260930",
  "plan": "../plans/AR-1335.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Generate and validate all supported ASB configuration files from reviewed TUI selections.",
  "task_revision": 12,
  "title": "ASB configuration materialization and preflight",
  "updated_at": "2026-09-30T11:47:44+00:00",
  "worktree_key": "asb-tui-ar-1335-configuration-materialization"
}
---

This AR owns asb-tui-side configuration materialization only; it does not modify the ASB repository.

- 2026-09-30T10:44:52+00:00: Dependencies AR-1333 and AR-1334 are done; begin configuration
  materialization and preflight.

- 2026-09-30T10:45:03+00:00: Claimed by tui-ar1335-dev-20260930.

- 2026-09-30T11:07:15+00:00: Exact-head repair 0ec8de4 adds catalog membership validation, provider
  review binding, private atomic sync, and focused drift/unknown-selection tests. PR #161 hosted
  checks must rerun; visible preflight/UI integration remains before merge.

- 2026-09-30T11:12:25+00:00: Exact head ed3db30 repairs provider review drift and benchmark
  membership validation, adds private sync protections and formal model/test updates. Independent
  review approved these repairs but still blocks merge on visible preflight route/apply integration.
  Hosted checks are rerunning on ed3db30.

- 2026-09-30T11:25:00+00:00: Signed commit 88d340f adds formal configuration.preflight
  element/action/help, visible digest-bound summary, and atomic apply_materialized_bundle UI seam.
  Local full test/clippy/formal/help/parity checks pass; hosted checks and independent review
  pending.

- 2026-09-30T11:29:16+00:00: Signed commits 5657c55 and a2cf726 make V build a reviewed bundle,
  retain it for explicit A apply, add formal apply transition/help, recover valid interrupted
  staging, and test corrupt-existing preservation. Full local tests/clippy pass; hosted checks and
  independent review pending.

- 2026-09-30T11:31:54+00:00: Signed 2ff45f7 binds preflight to an injected catalog-bound provider
  draft when available, refuses drift, and enforces 0600/fsync on recovered stage files. Local
  clippy and focused/full tests pass; hosted checks and review pending.

- 2026-09-30T11:38:57+00:00: Signed 987f29f registers OpenPreflight/ApplyPreflight in the
  authoritative action registry, emits them from V/A handling, and treats partial live catalogs as
  authoritative so development fallback cannot occur. Local focused tests pass; hosted CI/review
  pending.

- 2026-09-30T11:41:57+00:00: Signed 83d05e1 keeps local OpenPreflight/ApplyPreflight actions out of
  the backend recording dispatcher; authenticated interactive V/A now execute locally without
  InvalidWorkloadScope. Local focused test passes; hosted CI/review pending.

- 2026-09-30T11:43:16+00:00: Signed e36888b repairs help-overlay routing: contextual help keys
  remain local and no longer emit OpenPreflight. Focused help-key test passes; hosted CI/review
  pending.

- 2026-09-30T11:47:44+00:00: Signed cae7055 adds the canonical LaunchBinding API and handoff
  contract documentation, binding materialization digest, catalog generations/digests, exact IDs,
  and development provenance; adds a completeness/privacy test. Hosted CI previously exposed one
  flaky PTY test and was rerun.
