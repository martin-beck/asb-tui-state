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
  "observed_branch": "feature/ar1735-visual-route-resize-regression",
  "observed_dirty": 0,
  "observed_head": "3d978ba716f17ed9c11ca7f732c646e68a06ab7f",
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
  "task_revision": 8,
  "title": "Qualify visual fidelity across routes, resize, and terminal capabilities",
  "updated_at": "2026-10-13T02:34:41+00:00",
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

- 2026-10-13T02:34:18+00:00: Recorded command exit 0; command argv SHA-256
  272b6cb10709084b33ced1947aeb5f37195cf23369b85df5f895cfb596ee392b.

- 2026-10-13T02:34:26+00:00: Recorded command exit 0; command argv SHA-256
  f9911a459ed7ff14b3d418580d81f915ffbb7575c713e322edf715f1e65db495.

- 2026-10-13T02:34:37+00:00: Recorded command exit 0; command argv SHA-256
  a4346e5c9bd20ca0b01ba5e7e10c3a7c702a2535d6afc855a9227160f2120b66.
