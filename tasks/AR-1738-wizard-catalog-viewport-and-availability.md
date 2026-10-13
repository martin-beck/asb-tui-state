---
{
  "branch": "feature/ar1738-wizard-catalog-viewport-and-availability",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T14:08:40+00:00",
  "depends_on": [],
  "id": "AR-1738",
  "next_action": "Promote, claim an isolated current-main worktree, reproduce the catalog viewport and typed availability defects under a PTY, then implement and qualify the asb-tui repair.",
  "observed_branch": "feature/ar1738-wizard-catalog-viewport-and-availability",
  "observed_dirty": 4,
  "observed_head": "63400fdb3a06576145302a7d5ca596ac1e72f54d",
  "owner": "codex-asb-tui-ar1738-20261013",
  "plan": "../plans/AR-1738-wizard-catalog-viewport-and-availability.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1738.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the visible wizard agent picker: keep focus in the rendered viewport, use human labels rather than internal element IDs, and preserve typed catalog availability reasons.",
  "task_revision": 10,
  "title": "Repair wizard catalog viewport and availability presentation",
  "updated_at": "2026-10-13T12:13:05+00:00",
  "worktree_key": "asb-tui-ar-1738-wizard-catalog-viewport-and-availability"
}
---

The current renderer truncates catalog rows to eight but retains a cursor over
the full filtered list, so Down can move focus to a row that is not visible.
It also exposes the internal formal identifier `wizard.agent` as ordinary UI
text and discards the typed agent-catalog availability reason in favor of the
ambiguous sentence "not available for this setup".

This AR owns only asb-tui's state-to-presentation seam. It must not fabricate
an available agent, loosen ASB catalog validation, change ASB behavior, or
hide an unavailable catalog. ASB owns the launcher lifetime and catalog
production repairs separately.

- 2026-10-13T12:08:38+00:00: P0 user-reported wizard viewport, raw identifier, and typed
  availability repair is dependency-ready.

- 2026-10-13T12:08:40+00:00: Claimed by codex-asb-tui-ar1738-20261013.

- 2026-10-13T12:09:00+00:00: Recorded command exit 0; command argv SHA-256
  eeaa612e46ded265c56d84c305b781599899b658fc282f82ad5b3f5a8451feb9.

- 2026-10-13T12:09:06+00:00: Recorded command exit 0; command argv SHA-256
  7084f53da9a9f86d2905cd276ad7bf707161f1279ac868b69d1864c12a0bea9c.

- 2026-10-13T12:12:33+00:00: Recorded command exit 1; command argv SHA-256
  7ca4558f1330f6854210b691cb99c18e6c2f4261c4cbfc2a22ce72a274c39a73.

- 2026-10-13T12:12:50+00:00: Recorded command exit 0; command argv SHA-256
  a8ead32e951460d96f5ef53ad26f5f0381d0ad41b3580927aa87ff0757275af4.

- 2026-10-13T12:13:05+00:00: Recorded command exit 101; command argv SHA-256
  cd4b0d0b7c378e3f9c6661f6fe324fd9e72f639e38a1c9e002f7e5afd48122cb.
