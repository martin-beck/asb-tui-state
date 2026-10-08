# ASB TUI coordination state

This public repository is the Git-authoritative coordination state for
[`martin-beck/asb-tui`](https://github.com/martin-beck/asb-tui).

It currently vendors the exact `agent-workflow-coordinator` development commit
`e863b57edc7f7a21b2aff2c7b45ce226e12637d2` and tree
`eee603591b917eeca244425559d7c67bb88a7268` through the upstream
`sync-development` path and deliberately selects the tracked Markdown/Git backend. The schema-v2
manifest is development evidence, not release evidence. This state repository does not use or
create a SQLite authority database.

Read `AGENTS.md` and `docs/DEVELOPMENT.md` before operating the coordinator. Generated files such
as `CURRENT.md`, `STATUS.md`, `PROJECT_STATE.md`, and `WORKTREES.md` must never be edited directly.
The deterministic verification gate and the procedure for reconciling pre-bootstrap workers,
claiming isolated work, handling failures and publishing reviewed handoffs are documented in
[`docs/OPERATIONS.md`](docs/OPERATIONS.md).
