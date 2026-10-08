# ASB TUI coordination state

This public repository is the Git-authoritative coordination state for
[`martin-beck/asb-tui`](https://github.com/martin-beck/asb-tui).

It currently vendors the exact `agent-workflow-coordinator` development commit
`c2eb41879be4f2d50c6b5650e82339e10d5961d8` through the upstream
`sync-development` path and deliberately selects the tracked Markdown/Git backend. The schema-v2
manifest is development evidence, not release evidence. This state repository does not use or
create a SQLite authority database.

Read `AGENTS.md` and `docs/DEVELOPMENT.md` before operating the coordinator. Generated files such
as `CURRENT.md`, `STATUS.md`, `PROJECT_STATE.md`, and `WORKTREES.md` must never be edited directly.
The deterministic verification gate and the procedure for reconciling pre-bootstrap workers,
claiming isolated work, handling failures and publishing reviewed handoffs are documented in
[`docs/OPERATIONS.md`](docs/OPERATIONS.md).
