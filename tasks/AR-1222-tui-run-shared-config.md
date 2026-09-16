---
{
  "branch": "docs/ar-1222-tui-run-shared-config",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1221"
  ],
  "id": "AR-1222",
  "next_action": "Coordinator review PR #109 at exact head f607776; merge only after required checks and independent review pass.",
  "owner": "",
  "plan": "../plans/AR-1222.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Teach TUI users to run a benchmark and apply one configuration to multiple agents.",
  "task_revision": 5,
  "title": "asb-tui benchmark run and shared-agent configuration tutorials",
  "updated_at": "2026-09-16T12:35:11+00:00",
  "worktree_key": "asb-tui-ar-1222"
}
---

Implement the linked tutorials and offline fixtures. Tutorial CI must not perform a benchmark run.

- 2026-09-16T12:29:58+00:00: AR-1221 is merged and released done; promote the next standalone
  asb-tui tutorial task.

- 2026-09-16T12:30:45+00:00: Claimed by asb-tui-ar1222-tutorial-worker-20260916.

- 2026-09-16T12:35:08+00:00: Implementation pushed as PR #109 at exact signed/DCO head f607776.
  Added benchmark-run and shared-agent-configuration JSON/Markdown tutorials,
  running/cancelled/recovered and atomic applied/refused fixtures, and offline validator wired into
  Repository quality. Local checks: cargo +1.93.0 fmt --all --check; Python tutorial validators; git
  diff --check.

- 2026-09-16T12:35:11+00:00: Released for coordinator review: PR #109 exact head f607776, signed SSH
  ED25519 and DCO; no ASB changes.
