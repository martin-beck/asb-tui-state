---
{
  "branch": "repair/ar-1731-agent-picker-key-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1731",
  "next_action": "Promote and claim the wizard picker repair; make selection and continuation feedback explicit and PTY-tested.",
  "owner": "",
  "plan": "../plans/AR-1731-agent-picker-key-contract-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1731.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Make wizard agent selection and Enter continuation deterministic, visible, and self-explanatory in the installed TUI.",
  "task_revision": 1,
  "title": "Repair wizard agent-picker selection and continuation key contract",
  "updated_at": "2026-10-12T13:45:44+00:00",
  "worktree_key": "asb-tui-ar1731-agent-picker-key-contract"
}
---

The first-run wizard displays an Agent step but an operator can press Enter
with no visible selection and receive no actionable feedback. Selection is
currently assigned to Space while Enter is presented as continuation, yet the
runtime and formal transition behavior must make this distinction unambiguous
and accessible.

Repair the asb-tui application only. Preserve catalog-backed multi-selection,
search, unavailable-option diagnostics, formal state-machine authority, and
the existing explicit Space/select-all controls. An empty selection must never
silently advance or appear accepted. The focused repair must remain usable
when launched through the ASB development route once its separate AR-1800
launcher repair is available.
