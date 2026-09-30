---
{
  "branch": "feature/ar-1339-top-level-install-launch",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T12:37:47+00:00",
  "depends_on": [
    "AR-1200",
    "AR-1324",
    "AR-1327"
  ],
  "id": "AR-1339",
  "next_action": "Promote after the development router, onboarding, and qualification fixtures are complete; implement and qualify `asb tui install`, `asb tui`, status, upgrade, remove, and recovery.",
  "observed_branch": "feature/ar-1339-top-level-install-launch",
  "observed_dirty": 0,
  "observed_head": "e8c56a2e179f59cdf3be8d6442a8d127764777eb",
  "owner": "tui-ar1339-dev-20260930",
  "plan": "../plans/AR-1339.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the supported top-level ASB commands install and launch the standalone asb-tui application safely.",
  "task_revision": 7,
  "title": "Top-level ASB TUI install and launch integration",
  "updated_at": "2026-09-30T09:42:34+00:00",
  "worktree_key": "asb-tui-ar-1339-top-level-install-launch"
}
---

This AR belongs to the standalone asb-tui integration boundary; no ASB source changes are authorized here. Development fixture operation is sufficient for implementation and tests, but must never be mislabeled as production support.

- 2026-09-30T09:36:46+00:00: Dependencies AR-1200, AR-1324, and AR-1327 are done; begin top-level
  install/launch integration with development fixtures.

- 2026-09-30T09:37:47+00:00: Claimed by tui-ar1339-dev-20260930.

- 2026-09-30T09:38:04+00:00: Recorded command exit 0; command argv SHA-256
  1a92529b655347cec7a5296c99bb64ffeba589d903ee492ef3642d729cd8e0c6.

- 2026-09-30T09:42:29+00:00: Recorded command exit 0; command argv SHA-256
  d3c9bf2dddd8c7e875fe53193cd872a1f351345fe14da7d58e0a75295e8a14e9.
