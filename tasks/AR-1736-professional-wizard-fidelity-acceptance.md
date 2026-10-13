---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1735"
  ],
  "id": "AR-1736",
  "next_action": "Run an independently reviewed exact-head usability and fidelity acceptance journey across the installed asb-tui wizard.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1736-professional-wizard-fidelity-acceptance.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1736.json",
    "spec_revision": 1,
    "status": "planned"
  },
  "spec_ref": "specs/AR-1736.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Independently qualify that the installed wizard is visually professional, keyboard-discoverable, responsive, and truthful across the complete supported route.",
  "task_revision": 2,
  "title": "Accept professional wizard visual fidelity and usability",
  "updated_at": "2026-10-13T04:18:36+00:00",
  "worktree_key": "asb-tui-ar-1736-professional-wizard-fidelity-acceptance"
}
---

This acceptance AR verifies the rendered application, not only renderer unit
fixtures. It remains TUI-only and must not claim ASB provider/runtime behavior
that the backend has not supplied.

- 2026-10-13T04:18:36+00:00: AR-1735 is released with exact-main qualification; final installed TUI
  fidelity acceptance is dependency-ready.
