# AR-1739 plan: guided tools, agents, and workloads installation

1. Bind a versioned ASB control contract that enumerates installable tools,
   agents, and workloads with stable IDs, display labels, prerequisites,
   compatibility, current lifecycle state, typed failure reason, and
   provenance-safe progress. Reject missing, stale, malformed, or unsupported
   catalogs before rendering a selectable item.
2. Add a reachable first-run and reconfiguration TUI route with separate
   tool, agent, and workload sections, search, checkboxes, selected-summary,
   per-item help, and conventional keyboard controls. Show already-installed,
   unavailable, and pending items truthfully and distinctly.
3. Dispatch reviewed multi-item selections only through ASB-owned install,
   cancel, retry, refresh, and status operations. Keep install state bound to
   catalog generation and request identity; never execute a downloader,
   package manager, shell command, or compiler from the TUI.
4. Render bounded per-item progress, terminal success/failure/cancel states,
   and concise next steps. On successful agent/workload installation, refresh
   the authoritative setup catalog and return focus to the relevant wizard
   step without silently selecting an item.
5. Extend the formal UI model, generated model, help catalog, source/module
   ownership inventory, deterministic fixtures, and PTY/render tests for
   selection, progress, cancellation, retry, stale catalog, disconnected, and
   unavailable paths.
6. Qualify with exact paired ASB/asb-tui heads, independent exact-head review,
   signed-DCO commits, required CI, merge, and post-merge installed PTY
   evidence.

Done requires a new user to install supported prerequisites from the TUI and
then continue to setup using the freshly authoritative catalog, while all
acquisition and provenance decisions remain auditable ASB operations.
