---
{
  "branch": "feature/ar1202-live-resize-qualification",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1201"
  ],
  "id": "AR-1202",
  "next_action": "Promote after AR-1201 defines the model binding; review PR #65 at its exact head and implement/qualify live resize in the standalone asb-tui application.",
  "owner": "",
  "plan": "../plans/AR-1202.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Handle terminal resize safely across every asb-tui route without losing state or violating the formal model.",
  "task_revision": 8,
  "title": "Live terminal resize integration and qualification",
  "updated_at": "2026-09-25T12:36:18+00:00",
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

- 2026-09-25T12:25:14+00:00: Heartbeat by codex-asb-tui-ar1202-20260925.

- 2026-09-25T12:26:14+00:00: Recorded command exit 0; command argv SHA-256
  0a34898789f89b3416d159c8224a8a2182ebaa9354fa01a0cff1560050b67dd6.

- 2026-09-25T12:26:44+00:00: PR #142 pushed at signed head a7dd214. Local full locked Rust suite,
  clippy, formatting, formal model and source-parity checks, focused route-resize tests, TestBackend
  and PTY coverage pass. Hosted exact-head checks are pending; claim again for merge and post-merge
  verification.

- 2026-09-25T12:36:15+00:00: Claimed by codex-asb-tui-ar1202-merge-20260925.

- 2026-09-25T12:36:18+00:00: PR #142 merged at e6a9dd677d6be043d1d04d48310ba026ef022fa2 after
  exact-head hosted Repository quality and AWQ shadow checks passed. Local locked full suite,
  clippy, formatting, formal model generation/validation, source parity, TestBackend and PTY resize
  tests passed; AR-1201 remains the formal-model dependency.
