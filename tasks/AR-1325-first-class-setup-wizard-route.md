---
{
  "branch": "feature/ar-1325-first-class-setup-wizard-route",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1192",
    "AR-1197",
    "AR-1317",
    "AR-1321",
    "AR-1323",
    "AR-1324",
    "AR-1328"
  ],
  "id": "AR-1325",
  "next_action": "Promote after the helper handoff and development onboarding dependencies are done; bind wizard screens to the local setup contract and add restart/cancellation evidence.",
  "owner": "",
  "plan": "../plans/AR-1325.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Deliver a selection-driven first-run and reconfiguration wizard over the shared ASB setup contract.",
  "task_revision": 10,
  "title": "First-class setup wizard route",
  "updated_at": "2026-09-30T06:28:17+00:00",
  "worktree_key": "asb-tui-ar-1325-first-class-setup-wizard-route"
}
---

This is a standalone TUI development route. It must remain wire-compatible with local catalog,
credential-reference, and default-selection fixtures while clearly labeling development evidence.

- 2026-09-30T06:15:08+00:00: Development-only dependency chain is now unblocked: AR-1324 merged at
  dc36b28 and live/production gates were removed from this development workflow. Promote wizard
  route implementation.

- 2026-09-30T06:15:10+00:00: Claimed by tui-ar1325-dev-20261001.

- 2026-09-30T06:15:32+00:00: Recorded command exit 0; command argv SHA-256
  032e2d9795734edcdceb46f34c575db2740cc0a12d78b736e2362d7ff8005be7.

- 2026-09-30T06:17:29+00:00: Recorded command exit 0; command argv SHA-256
  2e9ba0c685dd98b0a74c5b2d861ceb62423a9f7bc1ce8261f901771053ffe581.

- 2026-09-30T06:17:56+00:00: Recorded command exit 0; command argv SHA-256
  60b0120aa3fa64a351159fc3cc121f7243fa45f0f658f399c2b720f0ed05abb8.

- 2026-09-30T06:18:18+00:00: Heartbeat by tui-ar1325-dev-20261001.

- 2026-09-30T06:23:00+00:00: Recorded command exit 0; command argv SHA-256
  d9d049fbd78f82f99cd2c5a654342c672f09dd7fe3e03034196b874f40cc6d65.

- 2026-09-30T06:25:56+00:00: Recorded command exit 0; command argv SHA-256
  20bdcf8cdb2a9b011588b940826e8c39e377589edc070fbc7dad26bd078033a4.

- 2026-09-30T06:28:17+00:00: Implemented and merged PR #155 at main
  ba0e3cee38acdfcc029339d9b43e306d8d41cc86. Exact hosted checks passed: Trusted main verification
  36678186406; Repository quality 36678186439. Independent review approved exact head 321ebf8.
