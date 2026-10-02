# AR-1659 — TUI materializer and installed handoff UX

Present the ASB-owned clone/build/materialize/install/launch lifecycle as a
small selectable flow. Show progress and exact revisions, permit cancellation,
preserve the prior install on failure, and explain rollback, remove, and
manifest/control incompatibility. Keep the TUI process isolated from build
artifacts and child-process leaks.
