---
{
  "branch": "feature/ar-1337-final-results-reports",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1336",
    "AR-1223"
  ],
  "id": "AR-1337",
  "next_action": "Await successful exact-main Trusted verification for merge SHA d7e5a53b9f7df0a2540b283baf6a6c8ee7a3db68; Repository Quality is green, then release AR-1337 and promote AR-1338.",
  "owner": "",
  "plan": "../plans/AR-1337.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Show final performance results, measure status, provenance, failures, and comparable recent runs.",
  "task_revision": 14,
  "title": "Final performance results and report presentation",
  "updated_at": "2026-09-30T14:46:55+00:00",
  "worktree_key": "asb-tui-ar-1337-final-results-reports"
}
---

Results must distinguish development, replay, live, unavailable, and unsupported evidence.

- 2026-09-30T13:53:14+00:00: AR-1336 live-statistics foundation is merged and exact-main Repository
  Quality plus Trusted main verification are green.

- 2026-09-30T13:53:17+00:00: Claimed by tui-ar1337-dev-20260930.

- 2026-09-30T13:54:19+00:00: Recorded command exit 0; command argv SHA-256
  9d4fb1971e8537df234621ae98ef5afd37bdcac53f8a96b0683427969d8df36e.

- 2026-09-30T13:57:03+00:00: Recorded command exit 0; command argv SHA-256
  acbd5aeb67a834a6c69a5eaf87a63112ae26752effb1b244e6bbea4bed499d92.

- 2026-09-30T13:59:46+00:00: Opened signed+DCO PR #175 at exact head
  dcaa6584b65e93c3ea2ffbc7a53779e7cec251c4. Local cargo test --all-targets and strict clippy pass.
  Added explicit evidence/status classes, compatibility identity fencing, bounded result validation,
  and actionable presentation rows.

- 2026-09-30T14:01:43+00:00: Independent review requested and fixed: comparison now fences
  EvidenceKind, and privacy projection rejects api-key, authorization, and Bearer forms with tests.
  Signed+DCO head 5f0f953; local tests and strict clippy pass.

- 2026-09-30T14:03:37+00:00: Recorded command exit 0; command argv SHA-256
  9ebb78d3dc1f63449fc43d7e373e493a3a44f57bc5b736fd54a71a7a6e5e2ab2.

- 2026-09-30T14:03:48+00:00: Recorded command exit 0; command argv SHA-256
  06d941468bbaf98d67456117394c9048af956063117f726f2b048783e7311991.

- 2026-09-30T14:11:52+00:00: Repaired formal CI gate: added reports.evidence, reports.measure, and
  reports.failure to authored/generated UI model with meaningful help text, and documented
  src/reports.rs ownership in UI module inventory. Signed+DCO commit 5bd8a99; local model validators
  and all-target tests pass.

- 2026-09-30T14:13:22+00:00: Completed formal help-catalog repair requested by CI/review: added
  meaningful reports.evidence, reports.measure, and reports.failure entries to docs/ui-help.json.
  Local validate-ui-state-model/test-ui-state-model and validate-ui-help/test-ui-help pass.
  Signed+DCO head 7db5090.

- 2026-09-30T14:17:56+00:00: Removed phantom reports.evidence/measure/failure formal elements that
  had no renderer-owned source bindings. Updated existing reports row/compare model and help text
  with evidence/status/provenance guidance, regenerated model, and retained reports.rs inventory
  responsibility. Signed+DCO head 007211d; local source/model/help validators and all-target tests
  pass.

- 2026-09-30T14:31:28+00:00: PR #175 merged as d7e5a53. Repository Quality passed; Trusted-main push
  and manual runs hit hosted self-hosted runner checkout/setup failures before tests, so release
  remains gated.

- 2026-09-30T14:46:55+00:00: PR #175 merged as d7e5a53b9f7df0a2540b283baf6a6c8ee7a3db68; Repository
  Quality 36728407200 green and Trusted main verification 36731426065 green after dedicated runner
  VM OOM repair.
