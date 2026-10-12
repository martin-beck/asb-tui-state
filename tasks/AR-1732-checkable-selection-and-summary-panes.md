---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T00:23:13+00:00",
  "depends_on": [
    "AR-1731"
  ],
  "id": "AR-1732",
  "next_action": "Implement accessible multi-selection controls with visible checked state, isolated selection summary, and well-structured descriptions.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-tui-ar1732-selection-20261013",
  "plan": "../plans/AR-1732-checkable-selection-and-summary-panes.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1732.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1732.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make all selectable wizard lists visibly checkable and separate selection summaries from contextual descriptions.",
  "task_revision": 5,
  "title": "Add checkable selections and separated wizard summary panes",
  "updated_at": "2026-10-12T22:54:21+00:00",
  "worktree_key": "asb-tui-ar-1732-checkable-selection-panes"
}
---

Selection must be legible at a glance: unchecked entries render `[ ]`, checked
entries render `[x]` or an equally unambiguous supported glyph, and focus is
visually distinct from selection.

- 2026-10-12T22:52:45+00:00: AR-1731 is released and exact-main-qualified; checkable selection work
  is now dependency-ready.

- 2026-10-12T22:53:13+00:00: Claimed by codex-asb-tui-ar1732-selection-20261013.

- 2026-10-12T22:54:17+00:00: Recorded command exit 0; command argv SHA-256
  0c87d5699a33c437d029322aa0714c3995ff9e34d86a99710e72ffc32c5084f3.

- 2026-10-12T22:54:21+00:00: Recorded command exit 0; command argv SHA-256
  ecd09cc9064a58fc23e2058d231def6f00860dc03122a18dda9e9661ac87e726.
