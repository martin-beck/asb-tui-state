---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1723"
  ],
  "id": "AR-1731",
  "next_action": "Define and implement the renderer-neutral visual language and persistent wizard shell before changing individual controls.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1731-visual-language-and-wizard-shell.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1731.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1731.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Create a professional, accessible ASB TUI visual language and persistent wizard shell informed by established high-value terminal UIs.",
  "task_revision": 2,
  "title": "Establish ASB TUI visual language and wizard shell",
  "updated_at": "2026-10-12T22:13:51+00:00",
  "worktree_key": "asb-tui-ar-1731-visual-language-shell"
}
---

Create the shared visual vocabulary used by every ASB TUI route. Reference
widely understood terminal UI conventions exemplified by k9s/lazygit-style
focused panes, status colors, compact key hints, and readable borders, without
copying their code, marks, or assets.

- 2026-10-12T22:13:51+00:00: AR-1723 is done; the merged visual-fidelity series makes this first
  implementation task dependency-ready.
