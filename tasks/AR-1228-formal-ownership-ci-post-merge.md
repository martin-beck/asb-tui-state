---
{
  "branch": "feature/ar1183-formal-ci",
  "checkpoint_commit": "d29ba818f21abd626efc85939f582edba685ac49",
  "claim_expires": "2026-09-15T13:03:23+00:00",
  "depends_on": [],
  "id": "AR-1228",
  "next_action": "Record exact post-merge workflow conclusions for corrected PR #71.",
  "owner": "root-formal-merge-watch",
  "plan": "../plans/AR-1228.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify formal UI ownership CI after merge.",
  "task_revision": 2,
  "title": "Formal ownership CI post-merge assurance",
  "updated_at": "2026-09-15T11:03:23+00:00",
  "worktree_key": "asb-tui-formal-ownership-ci-post-merge"
}
---

PR #71 was corrected for malformed route/transition/element shapes and relocatable tests, rebuilt
with SSH/DCO-signed commits, and merged at immutable main SHA
`d29ba818f21abd626efc85939f582edba685ac49`. The required exact-main Repository quality and Trusted
main workflows are being watched here. This gate does not claim full runtime/model parity; AR-1201
remains authoritative for that work.

- 2026-09-15T11:03:23+00:00: Claimed by root-formal-merge-watch.
