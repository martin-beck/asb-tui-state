---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-14T09:59:06+00:00",
  "depends_on": [],
  "id": "AR-1740",
  "next_action": "Verify the exact v0.7.11 release identity and vendor the complete allowlisted snapshot through the official synchronizer in an isolated current-main state worktree.",
  "owner": "asb-tui-state-ar1740-v0711-20261014",
  "plan": "../plans/AR-1740-coordinator-v0711-release-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1740.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the exact Agent Workflow Coordinator v0.7.11 release and qualify ASB-TUI state compatibility.",
  "task_revision": 4,
  "title": "Coordinator v0.7.11 release vendor for ASB-TUI state",
  "updated_at": "2026-10-14T06:59:24+00:00",
  "worktree_key": ""
}
---

Upgrade the ASB-TUI coordination-state vendor from Coordinator v0.4.0 to the
latest upstream release v0.7.11. The downstream state remains Git-authoritative
and must retain its binding, task history, privacy policy, and all unrelated
work unchanged.

The upstream v0.7.11 lightweight tag resolves to commit
`6f7cb5eeb411898c7812fdebc9da08e1f586c936` and tree
`7a1aa2e956742bb1382a584c9c2f38f1794af815`. Record the lightweight-tag
provenance accurately; do not make an annotated-tag signature claim.


- 2026-10-14T06:59:03+00:00: Upstream v0.7.11 release identity is refreshed and the dedicated
  vendor-upgrade scope is dependency-ready.

- 2026-10-14T06:59:06+00:00: Claimed by asb-tui-state-ar1740-v0711-20261014.

- 2026-10-14T06:59:24+00:00: Recorded command exit 0; command argv SHA-256
  a889c9966cfe28a4891c3a4b0379d0fad9ac2e854ab214adc56b6d5b7fea4e30.
