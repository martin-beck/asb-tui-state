---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1739",
  "next_action": "Define and consume the versioned ASB installation catalog and lifecycle contract, then promote when the required ASB command surface is available for the selected current-main pair.",
  "observed_branch": "",
  "observed_dirty": false,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1739-guided-tool-agent-workload-installation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1739.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Add a guided TUI route that lets users select and install supported tools, coding agents, and workloads through ASB-owned lifecycle operations before setup.",
  "task_revision": 1,
  "title": "Guided tools, agents, and workloads installation",
  "updated_at": "2026-10-13T12:35:00+00:00",
  "worktree_key": ""
}
---

The wizard must offer an explicit installation route before configuration and
later from reconfiguration. It displays the ASB-owned supported catalog of
tools, coding agents, and workloads; permits multi-selection; dispatches only
versioned ASB installation lifecycle requests; presents per-item progress,
success, cancellation, and actionable typed failure; and refreshes the setup
catalog after a completed installation.

asb-tui is a presentation and orchestration client. It must not download,
compile, resolve packages, persist secrets, claim installation success, or
invent availability locally. Those operations and their provenance remain ASB
responsibilities.
