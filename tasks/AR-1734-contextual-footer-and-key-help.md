---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1731",
    "AR-1732",
    "AR-1733"
  ],
  "id": "AR-1734",
  "next_action": "Render focus-aware concise footer help and a discoverable context-sensitive hotkey overlay for every current element and action.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1734-contextual-footer-and-key-help.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1734.json",
    "spec_revision": 1,
    "status": "planned"
  },
  "spec_ref": "specs/AR-1734.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Add a context-sensitive footer and hotkey overlay that explain the highlighted or hovered item and available actions.",
  "task_revision": 2,
  "title": "Render contextual footer help and current hotkeys",
  "updated_at": "2026-10-13T00:45:20+00:00",
  "worktree_key": "asb-tui-ar-1734-contextual-footer-hotkeys"
}
---

Existing document-backed help remains authoritative. This AR makes that help
immediately usable in the visual shell, rather than requiring a separate
documentation lookup.

- 2026-10-13T00:45:20+00:00: AR-1731 through AR-1733 are released; contextual help implementation is
  dependency-ready.
