---
{
  "branch": "feature/ar1201-formal-ui-source-parity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T14:08:45+00:00",
  "depends_on": [
    "AR-1197"
  ],
  "id": "AR-1201",
  "next_action": "Promote after AR-1197 and inventory prerequisites are reviewed; implement the executable model/source parity manifest and CI gate in asb-tui.",
  "owner": "codex-asb-tui-ar1201-20260925",
  "plan": "../plans/AR-1201.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make every TUI source element and transition mechanically checkable against the formal UI model.",
  "task_revision": 3,
  "title": "Executable formal UI model and source parity",
  "updated_at": "2026-09-25T12:08:45+00:00",
  "worktree_key": "asb-tui-ar-1201-formal-ui-source-parity"
}
---

Define and enforce a single authoritative, machine-readable inventory for standalone asb-tui UI
windows, elements, actions, routes, states, transitions, ownership, and contextual help. The
formal state/transition model and executable application source must be checked in both
directions: every model element/transition must have an implementation binding, and every
user-facing source element/action/route must be declared in the model. No render-only or hidden
escape hatch may bypass the model.

Relevant existing candidates are PR #70 (formal UI model), PR #71 (formal ownership CI), PR #74
(executable transitions), PR #77 (wizard state machine), PR #81 (UI inventory synchronization),
and PR #87 (startup decision). They are historical/open candidates, not completion evidence.
All application, model, renderer, and test changes belong in `martin-beck/asb-tui`; ASB must not
gain Ratatui, rendering, or application code.

Implementation requirements:

- Specify a versioned schema for stable element/action/state/transition IDs, ownership/module
  bindings, visibility predicates, reachable routes, and help-catalog IDs.
- Generate or validate the source inventory from the actual Rust modules/registrations, with no
  hand-maintained allowlist that can silently omit newly added UI code.
- Validate model-to-source and source-to-model equality, duplicate/unknown IDs, unreachable
  states, transitions lacking guards/effects, actions lacking handlers, and help/owner omissions.
- Keep the formal model and executable transition interpreter tied to the same identifiers and
  state-change semantics; changes must update the model and fail CI until the implementation and
  tests are updated together.
- Add deterministic model/property tests for reachability, forbidden transitions, startup,
  wizard, landing, configuration, reports, help, resize, reconnect, and error paths, plus
  renderer/TestBackend parity assertions for every declared element.
- Make CI run the parity validator and all model/property/parity tests on every UI or model change,
  and fail closed on schema/version drift. Record the exact source/model revision and commands.

Acceptance requires exact-head source review, signed DCO/SSH verification, full hosted CI, no
ASB UI code, and evidence that adding/removing/renaming an element or transition causes the
appropriate parity test to fail until both sides and its meaningful contextual help are updated.
Do not claim completion from a formal file existing or from a one-sided ownership check.

- 2026-09-25T12:08:42+00:00: AR-1197 is done; promoting dependency-ready formal UI parity work for
  asb-tui implementation.

- 2026-09-25T12:08:45+00:00: Claimed by codex-asb-tui-ar1201-20260925.
