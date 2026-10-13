---
{
  "branch": "feature/ar1738-wizard-catalog-viewport-and-availability",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T14:08:40+00:00",
  "depends_on": [],
  "id": "AR-1738",
  "next_action": "Promote, claim an isolated current-main worktree, reproduce the catalog viewport and typed availability defects under a PTY, then implement and qualify the asb-tui repair.",
  "observed_branch": "",
  "observed_dirty": false,
  "observed_head": "",
  "owner": "codex-asb-tui-ar1738-20261013",
  "plan": "../plans/AR-1738-wizard-catalog-viewport-and-availability.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1738.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the visible wizard agent picker: keep focus in the rendered viewport, use human labels rather than internal element IDs, and preserve typed catalog availability reasons.",
  "task_revision": 3,
  "title": "Repair wizard catalog viewport and availability presentation",
  "updated_at": "2026-10-13T12:08:40+00:00",
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
