# Coordinated development

This state installation is permanently bound to `martin-beck/asb-tui` and uses
`coordinator.backend.json` with backend `git`. The public task and plan files are the authority.

## Safe operating loop

1. Inventory current GitHub refs, pull requests, local worktrees, processes and claims.
2. Run `tools/handoffctl snapshot` and read the complete task and plan.
3. Claim one dependency-ready open task with a stable unique owner.
4. Create or reuse only the task's registered isolated worktree from exact current upstream main.
5. Run every mutation with `tools/handoffctl run --owner OWNER AR-NNNN -- COMMAND`.
6. Preserve native project gates when adding shared quality checks.
7. Require exact-head tests, privacy review, SSH signature, DCO and independent review before push
   or merge.
8. Release or update the task, then reconcile and run `tools/handoffctl doctor --live`.

The coordinator bootstrap does not authorize interruption, adoption or replacement of autonomous
workers that began before this repository existed. Wait for their durable handoff, then explicitly
check for overlapping paths and commits before any new claim or worker launch.
