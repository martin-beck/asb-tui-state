---
{
  "branch": "docs/ar-1220-first-run-agent",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1220",
  "next_action": "Promote after ASB tutorial-contract review; write the syntax-checked asb-tui first-run and first-agent tutorial.",
  "owner": "",
  "plan": "../plans/AR-1220.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Teach first-time users to initialize asb-tui and configure their first agent connection.",
  "task_revision": 2,
  "title": "asb-tui first-run and first-agent tutorial",
  "updated_at": "2026-09-16T11:59:22+00:00",
  "worktree_key": "asb-tui-ar-1220"
}
---

Implement the linked tutorial and offline route/state fixtures. Cross-repository dependency on ASB
AR-1210 is recorded in the plan; do not run tutorial actions or connect to an agent in CI.

- 2026-09-16T11:59:22+00:00: ASB tutorial contract is now published by merged ASB PR #184 at
  4d4a0c4f3bd71f9884c9cc06649ba6722fa03bff. AR-1220 remains synthetic/offline and does not require
  live ASB catalog/lifecycle execution.
