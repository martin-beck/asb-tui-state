# Git-backed coordinator operations

This repository is the public coordination authority for `martin-beck/asb-tui`. Task Markdown and
signed Git history are authoritative. `coordinator.backend.json` permanently selects `git`; a
SQLite database is neither an authority nor an operational fallback.

## Deterministic checks and live observations

Run the deterministic gate before requesting review:

```console
$ python3 tools/handoffctl_vendor.py verify --target .
$ python3 tools/check_source_headers.py
$ python3 -m unittest discover -s tests -p 'test_*.py'
$ tools/handoffctl doctor
$ tools/handoffctl render-status --check
```

These commands validate the vendored v0.3.5 snapshot, immutable project identities, explicit Git
backend, task graph, privacy policy, generated views and failure-path tests. They must not create
`.runtime/coordinator.sqlite3` or its journal files. A clean deterministic result says nothing about
changing GitHub state.

Use `tools/handoffctl snapshot` and `tools/handoffctl doctor --live` separately for bounded current
observations. Record an external API outage as an observation failure, not as task-graph corruption.

## Reconcile work that predates the coordinator

Do not interrupt, claim or reproduce work begun before this coordinator was installed. Before a new
claim, inventory active agent processes, registered Git worktrees, local branches, commits, dirty
paths, remote branches and pull requests. Accept a handoff only when it has a durable identity: a
commit, branch, pull request, or an explicitly documented dirty-state recovery target with its exact
base and affected paths.

For each handoff:

1. Record exact base and head revisions and the owning branch or worktree key.
2. Compare changed paths with the proposed AR's owned paths.
3. Preserve ambiguous or dirty effects in place and stop; do not discard or duplicate them.
4. Require review of the durable handoff before starting overlapping work.
5. Reconcile the coordinator, then confirm `tools/handoffctl doctor --live` succeeds.

Coordinator bootstrap is not permission to adopt another agent's work. No worker is launched merely
because an AR exists or a lease is available.

## Start and operate one worker

Read `AGENTS.md`, `docs/DEVELOPMENT.md`, the complete task and its plan. Select one dependency-ready
open AR and claim it with a stable, unique owner. Use only the task's registered branch and isolated
worktree, created from the exact current upstream base after overlap checks.

Every product, Git, review and publication mutation is fenced by the live claim:

```console
$ tools/handoffctl run --owner OWNER AR-NNNN -- COMMAND...
```

Heartbeat a worker that is actively progressing, and update the task with concise conclusions and
immutable public identifiers. A lease alone is not evidence of a running worker. On interruption,
inspect durable effects before retrying. Duplicate claims, one owner holding multiple active tasks,
duplicate branch/worktree allocation, stale task revisions, expired claims, wrong-repository
invocation, reconciliation failure, signature failure, push rejection and remote divergence all
fail closed and require explicit recovery.

Before publication, test the exact candidate head, run privacy and secret checks, obtain independent
review, create an SSH-signed commit with the matching `Signed-off-by` trailer, and push through the
wrapper. Never merge from a worker session. Update or release the AR, reconcile, and finish with a
live doctor check.

## Cross-project authority

Wizard work remains authoritative in `martin-beck/agent-systems-benchmark-state`, including the ASB
runner/API work in AR-1140 and AR-1160, the standalone frontend journey in AR-1170, and
cross-project qualification in AR-1180. References here express consumed contracts only. They do not
copy those ARs, change their owner or status, or authorize changes to the ASB product repository.
