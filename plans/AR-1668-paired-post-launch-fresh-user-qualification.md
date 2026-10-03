# AR-1668 — paired TUI post-launch fresh-user journey qualification

Run the complete exact-head ASB/TUI journey after the paired dev-release
dependencies: install the default `dev` channel, configure OpenRouter through
the TUI wizard, select `opencode`/`opendesk` and compatible models, persist
shared defaults, benchmark, record selected and all workloads, deny network
access, replay the recorded cassette offline, compare and analyze results,
exercise rollback-preserving upgrade and removal, and clean the disposable
workspace.

The receipt must include human and JSON outcomes, PTY evidence, exact ASB/TUI
heads and trees, provider/authentication/agent/model/workload/default
selection, cassette and result digests, network-denial evidence, warning-only
development authentication/signature/key-management status, and cleanup.

PR253 is a candidate implementation dependency/evidence source only. This AR
remains planned until its dependencies are released, the candidate is merged
with hosted checks, and the complete journey is rerun at the merged heads.
