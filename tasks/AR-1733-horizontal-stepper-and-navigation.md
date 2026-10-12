---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T00:23:15+00:00",
  "depends_on": [
    "AR-1731"
  ],
  "id": "AR-1733",
  "next_action": "Implement a formal-model-backed horizontal wizard stepper, current-step highlight, and conventional keyboard navigation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-tui-ar1733-stepper-20261013",
  "plan": "../plans/AR-1733-horizontal-stepper-and-navigation.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1733.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1733.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Show the complete wizard journey as a responsive horizontal stepper with current, complete, unavailable, and future step states.",
  "task_revision": 3,
  "title": "Add horizontal wizard stepper and conventional navigation",
  "updated_at": "2026-10-12T22:53:15+00:00",
  "worktree_key": "asb-tui-ar-1733-horizontal-stepper-navigation"
}
---

The top header must make progress and location visible: completed, current,
future, and blocked/unavailable steps remain distinguishable without color.

- 2026-10-12T22:52:48+00:00: AR-1731 is released and exact-main-qualified; horizontal stepper work
  is now dependency-ready.

- 2026-10-12T22:53:15+00:00: Claimed by codex-asb-tui-ar1733-stepper-20261013.
