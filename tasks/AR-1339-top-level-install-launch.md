---
{
  "branch": "feature/ar-1339-top-level-install-launch",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1200",
    "AR-1324",
    "AR-1327"
  ],
  "id": "AR-1339",
  "next_action": "PR #158 is green at exact head d47b27a; obtain independent review, merge, watch post-merge checks, then release.",
  "observed_branch": "feature/ar-1339-top-level-install-launch",
  "observed_dirty": 0,
  "observed_head": "d47b27a7beff96fafde62184668e29031d0b11ef",
  "owner": "",
  "plan": "../plans/AR-1339.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Make the supported top-level ASB commands install and launch the standalone asb-tui application safely.",
  "task_revision": 13,
  "title": "Top-level ASB TUI install and launch integration",
  "updated_at": "2026-09-30T09:51:10+00:00",
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

- 2026-09-30T09:43:37+00:00: Heartbeat by tui-ar1339-dev-20260930.

- 2026-09-30T09:44:50+00:00: Recorded command exit 0; command argv SHA-256
  2621aba9c3c2dff3ec4d708f8063b1f851a425f393ce4611efa94fd6176310ed.

- 2026-09-30T09:47:32+00:00: Standalone command adapter and development router integration are
  implemented; local and hosted checks pass. Awaiting independent exact-head review before merge.

- 2026-09-30T09:48:37+00:00: Recorded command exit 0; command argv SHA-256
  f0649951a2652bb389102a56ca172f4ca4f7e6390e70be164fd5a557717b616d.

- 2026-09-30T09:51:10+00:00: Implemented top-level standalone `tui` adapter in PR #158. Exact merged
  main 9b433f163953d6b4dcf8427cae3c1f7fb15babcd; repaired header failure at PR head d47b27a7,
  independently approved. Post-merge Repository quality 36698458426 and Trusted main verification
  36698458470 passed. Development operations require explicit --development --format json;
  production is fail-closed.
