---
{
  "branch": "feature/ar-1192-authenticated-agent-wizard",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T22:32:52+00:00",
  "depends_on": [],
  "id": "AR-1192",
  "next_action": "Do not wire lifecycle UI calls yet: ASB origin 2117a40 still returns CapabilityUnavailable for agent_catalog and agent lifecycle methods. Await authenticated ASB backend implementation, capability signaling, reconciled schemas/fixtures, and green exact-head/post-merge evidence; then adapt through the adopted broker stream in asb-tui.",
  "owner": "root",
  "plan": "../plans/AR-1192.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Consume authenticated ASB agent catalog and lifecycle in the standalone wizard.",
  "task_revision": 12,
  "title": "Authenticated agent wizard integration",
  "updated_at": "2026-09-15T21:32:52+00:00",
  "worktree_key": "asb-tui-ar-1192-authenticated-agent-wizard"
}
---

Implement the standalone UI integration in the linked plan after the ASB protocol dependencies are
published. All rendering and application behavior remains in asb-tui.

- 2026-09-15T15:40:43+00:00: Promote for tracking merged renderer-neutral catalog integration and
  remaining authenticated runtime work.

- 2026-09-15T15:40:46+00:00: Claimed by root.

- 2026-09-15T15:40:57+00:00: PR #103 merged into asb-tui main at 249591f after genuine PR CI
  34989446540; post-merge Repository quality 34989738729 and Trusted main verification 34989738764
  both passed. Catalog choices are compatible and bounded; authenticated runtime/install remains
  open.

- 2026-09-15T16:13:38+00:00: Heartbeat by root.

- 2026-09-15T16:14:47+00:00: 2026-09-15 live dependency audit: asb-tui main 9ab1201 and post-merge
  runs 34991922793/34991922837 are green. ASB catalog dependencies AR-1190/1191 are done, but router
  contract AR-1199 is not published; ASB PR #171 head 200edbb has failed Platform evidence run
  34945266711 (native_evidence.py: source identity is not immutable), so authenticated lifecycle
  integration remains gated.

- 2026-09-15T16:22:09+00:00: 2026-09-15 live refresh: ASB lifecycle router PR #157 merged as 967a4a7
  with all listed checks successful; catalog digest PR #174 merged as d354a51. The prior open PR
  #171 is a stale duplicate with a failed synthetic-base platform check and is not a dependency
  candidate. Readiness producer AR-1227 and cross-repo qualification remain unresolved.

- 2026-09-15T16:24:28+00:00: Router audit completed against ASB origin 2117a40: top-level lifecycle
  router PR #157 is merged, but asb-control backend agent_catalog and
  agent_install/status/cancel/retry/remove remain explicit CapabilityUnavailable and Capabilities
  has no lifecycle/catalog fields. The hidden asb-tui v1.5 candidate is not on main and must not be
  imported against rejecting backend. No implementation PR created.

- 2026-09-15T16:29:50+00:00: Heartbeat by root.

- 2026-09-15T16:31:46+00:00: Heartbeat by root.

- 2026-09-15T21:32:35+00:00: Recovered expired claim formerly owned by root. Recover expired root
  lease before re-evaluating ASB backend progress

- 2026-09-15T21:32:52+00:00: Claimed by root.
