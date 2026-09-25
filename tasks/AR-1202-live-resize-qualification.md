---
{
  "branch": "feature/ar1202-live-resize-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T14:23:11+00:00",
  "depends_on": [
    "AR-1201"
  ],
  "id": "AR-1202",
  "next_action": "Promote after AR-1201 defines the model binding; review PR #65 at its exact head and implement/qualify live resize in the standalone asb-tui application.",
  "owner": "codex-asb-tui-ar1202-20260925",
  "plan": "../plans/AR-1202.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Handle terminal resize safely across every asb-tui route without losing state or violating the formal model.",
  "task_revision": 3,
  "title": "Live terminal resize integration and qualification",
  "updated_at": "2026-09-25T12:23:11+00:00",
  "worktree_key": "asb-tui-ar-1202-live-resize"
}
---

Implement and qualify live terminal resize for the standalone asb-tui application. PR #65
(`feature/ar1038-live-resize`, exact candidate recorded in project state as
`b2db201a4187...`) preserves workspace state across resize but is not by itself evidence of
complete integration. Resize must be represented as a formal event/transition and must preserve
the currently selected route, focused element, drafts, report comparison context, wizard progress,
and pending safe operations. It must never fabricate state, panic, expose credentials, or leave the
terminal in a damaged mode.

All application, terminal/rendering, formal-model, and test work belongs in
`martin-beck/asb-tui`; ASB remains renderer-neutral and backend-only.

Implementation and qualification requirements:

- Convert authoritative terminal resize events into validated model events, rejecting impossible
  dimensions and coalescing/stabilizing resize storms without dropping the final size.
- Recompute layout and hot-key/context-help visibility for every route while retaining model state,
  focus, selection, scroll position, drafts, and pending operation identity.
- Define behavior for minimum dimensions: bounded readable fallback, actionable explanation, and
  safe restoration on recovery; never render outside the terminal or claim a successful action.
- Cover landing, wizard/configuration, measurement selection, report/history/comparison, help,
  error/reconnect, and pending lifecycle operations, including resize during transitions.
- Add deterministic TestBackend/model/property tests and PTY/integration tests for single resize,
  rapid storms, too-small/invalid dimensions, resize during input and transitions, reconnect and
  restart, terminal restoration, and final-state preservation.
- Add CI checks proving resize events and all affected source/model/ownership/help bindings remain
  synchronized under AR-1201; record platform capability limitations explicitly and fail closed.

Acceptance requires exact-head review of PR #65 and its dependencies, signed DCO/SSH verification,
full hosted CI, model/source parity, no ASB UI code, and reproducible evidence that every resize
path is safe and usable. A one-time terminal-size snapshot or unit test alone is insufficient.

- 2026-09-25T12:23:08+00:00: AR-1201 is done and source/model parity is now enforced on main;
  promote resize qualification.

- 2026-09-25T12:23:11+00:00: Claimed by codex-asb-tui-ar1202-20260925.
