# ASB TUI coordination state

This public repository is the Git-authoritative coordination state for
[`martin-beck/asb-tui`](https://github.com/martin-beck/asb-tui).

It currently vendors the exact `agent-workflow-coordinator` v0.4.0 release commit
`712b36ea3d188237cbe8104e70d905094f93a96b` and tree
`c496306050a805111f89b3f7bc4cfb0910f27535` through the upstream release `sync` path and
deliberately selects the tracked Markdown/Git backend. The upstream `v0.4.0` ref is a lightweight
tag; this repository binds the verified commit/tree and makes no annotated-tag signature claim.
The schema-v1 manifest is release-vendor evidence. This state repository does not use or create a
SQLite authority database.

Read `AGENTS.md` and `docs/DEVELOPMENT.md` before operating the coordinator. Generated files such
as `CURRENT.md`, `STATUS.md`, `PROJECT_STATE.md`, and `WORKTREES.md` must never be edited directly.
The deterministic verification gate and the procedure for reconciling pre-bootstrap workers,
claiming isolated work, handling failures and publishing reviewed handoffs are documented in
[`docs/OPERATIONS.md`](docs/OPERATIONS.md).
