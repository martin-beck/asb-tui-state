---
{
  "branch": "ci/ar-1224-tutorial-freshness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T13:26:59+00:00",
  "depends_on": [
    "AR-1220",
    "AR-1221",
    "AR-1222",
    "AR-1223"
  ],
  "id": "AR-1224",
  "next_action": "Implement the cross-repository tutorial discovery and syntax-freshness CI gate after the TUI tutorial contracts are defined.",
  "owner": "asb-tui-ar1224-freshness-20260916",
  "plan": "../plans/AR-1224.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Keep asb-tui tutorial routes, actions, commands, and schemas syntactically current in CI.",
  "task_revision": 6,
  "title": "Cross-repository tutorial syntax and freshness gate",
  "updated_at": "2026-09-16T12:56:59+00:00",
  "worktree_key": "asb-tui-ar-1224"
}
---

Implement the linked CI gate. It must validate syntax and synthetic fixtures only, with no ASB,
provider, LLM, benchmark, credential, or network execution.

- 2026-09-16T12:48:58+00:00: AR-1220 through AR-1223 are merged and released; promote tutorial
  freshness CI.

- 2026-09-16T12:49:57+00:00: Claimed by asb-tui-ar1224-freshness-20260916.

- 2026-09-16T12:54:27+00:00: Heartbeat by asb-tui-ar1224-freshness-20260916.

- 2026-09-16T12:54:29+00:00: Implementation complete for review in asb-tui PR #111 at
  71e54e1d6b349c25774ddbb74a687609ede306de. Validator discovers all six tutorial contracts, consumes
  ASB command metadata from immutable contract checkout 3e475bda8f44836a169bc8fc679b430f6c993961,
  checks paired docs/references/routes and offline safety without execution. Focused checks pass;
  cargo unavailable locally.

- 2026-09-16T12:56:59+00:00: Claimed by asb-tui-ar1224-freshness-20260916.
