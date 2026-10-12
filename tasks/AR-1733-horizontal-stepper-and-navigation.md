---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T00:55:16+00:00",
  "depends_on": [
    "AR-1731"
  ],
  "id": "AR-1733",
  "next_action": "Implement a formal-model-backed horizontal wizard stepper, current-step highlight, and conventional keyboard navigation.",
  "observed_branch": "feature/ar1733-horizontal-stepper-navigation",
  "observed_dirty": 2,
  "observed_head": "4fd9d2b84a228828961732e81d163c6f11df9117",
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
  "task_revision": 12,
  "title": "Add horizontal wizard stepper and conventional navigation",
  "updated_at": "2026-10-12T23:08:53+00:00",
  "worktree_key": "asb-tui-ar-1733-horizontal-stepper-navigation"
}
---

The top header must make progress and location visible: completed, current,
future, and blocked/unavailable steps remain distinguishable without color.

- 2026-10-12T22:52:48+00:00: AR-1731 is released and exact-main-qualified; horizontal stepper work
  is now dependency-ready.

- 2026-10-12T22:53:15+00:00: Claimed by codex-asb-tui-ar1733-stepper-20261013.

- 2026-10-12T22:55:16+00:00: Heartbeat by codex-asb-tui-ar1733-stepper-20261013.

- 2026-10-12T22:55:34+00:00: Recorded command exit 0; command argv SHA-256
  622f243221cc7dab684c85b5cad6644b95ebec3c08d81c5ba2aee4247072c5fb.

- 2026-10-12T22:57:01+00:00: Recorded command exit 0; command argv SHA-256
  63ff4d21591561c74c3a91ed7772417c45bd6267057d62528ee6459b317abb82.

- 2026-10-12T23:08:14+00:00: Recorded command exit 1; command argv SHA-256
  ba9c451f7ba761373ab9766cbecdd2914b104384338037efd14a13c5c250e37c.

- 2026-10-12T23:08:32+00:00: Recorded command exit 0; command argv SHA-256
  6cf781a2335fbaf266bd55e4431898d47513b7af549ffa625641d6796e09581f.

- 2026-10-12T23:08:53+00:00: Recorded command exit 0; command argv SHA-256
  79f4902302529f9d8c9f72f1fbef13cff774ff1f26f54a22ff86c6ee15fcc9c6.
