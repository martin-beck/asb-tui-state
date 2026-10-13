---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T05:33:40+00:00",
  "depends_on": [
    "AR-1732",
    "AR-1733",
    "AR-1734"
  ],
  "id": "AR-1735",
  "next_action": "Add deterministic visual-route, resize, accessibility, and formal parity regression coverage for the new fidelity system.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-tui-ar1735-visual-regression-20261013",
  "plan": "../plans/AR-1735-visual-route-and-resize-regression.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1735.json",
    "spec_revision": 1,
    "status": "planned"
  },
  "spec_ref": "specs/AR-1735.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Qualify the visual fidelity contract across every route, terminal size, color capability, and keyboard-only interaction without source/model/help drift.",
  "task_revision": 4,
  "title": "Qualify visual fidelity across routes, resize, and terminal capabilities",
  "updated_at": "2026-10-13T02:34:04+00:00",
  "worktree_key": "asb-tui-ar-1735-visual-route-resize-regression"
}
---

Visual regressions are product regressions: snapshots must prove hierarchy,
selection visibility, step location, footer help, and small-terminal behavior,
not merely that drawing does not panic.

- 2026-10-13T02:33:37+00:00: AR-1732 through AR-1734 are released; visual regression qualification
  is dependency-ready.

- 2026-10-13T02:33:40+00:00: Claimed by codex-asb-tui-ar1735-visual-regression-20261013.

- 2026-10-13T02:34:04+00:00: Recorded command exit 0; command argv SHA-256
  888e6a0a261cf859bbde85a162a1168960ada0fa6e00053ffc37a21145a22d37.
