---
{
  "branch": "ci/ar-1224-tutorial-freshness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1220", "AR-1221", "AR-1222", "AR-1223"],
  "id": "AR-1224",
  "next_action": "Implement the cross-repository tutorial discovery and syntax-freshness CI gate after the TUI tutorial contracts are defined.",
  "owner": "",
  "plan": "../plans/AR-1224.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Keep asb-tui tutorial routes, actions, commands, and schemas syntactically current in CI.",
  "task_revision": 1,
  "title": "Cross-repository tutorial syntax and freshness gate",
  "updated_at": "2026-09-15T00:00:00+00:00",
  "worktree_key": "asb-tui-ar-1224"
}
---

Implement the linked CI gate. It must validate syntax and synthetic fixtures only, with no ASB,
provider, LLM, benchmark, credential, or network execution.
