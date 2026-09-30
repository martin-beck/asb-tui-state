---
{
  "branch": "feature/ar-1337-final-results-reports",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T17:53:17+00:00",
  "depends_on": [
    "AR-1336",
    "AR-1223"
  ],
  "id": "AR-1337",
  "next_action": "Await exact-head hosted checks and independent review for PR #175 at 5f0f953; merge only after all required gates pass.",
  "owner": "tui-ar1337-dev-20260930",
  "plan": "../plans/AR-1337.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Show final performance results, measure status, provenance, failures, and comparable recent runs.",
  "task_revision": 7,
  "title": "Final performance results and report presentation",
  "updated_at": "2026-09-30T14:01:43+00:00",
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
