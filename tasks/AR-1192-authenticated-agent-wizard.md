---
{
  "branch": "feature/ar-1192-authenticated-agent-wizard",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T17:13:38+00:00",
  "depends_on": [],
  "id": "AR-1192",
  "next_action": "Audit and implement the authenticated catalog/lifecycle client against ASB router merge 967a4a7a0501231b1fed37a37a784d8ab1e42c07; verify readiness/configuration contracts and cross-repository pins before wiring install. Keep all renderer/application work in asb-tui.",
  "owner": "root",
  "plan": "../plans/AR-1192.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Consume authenticated ASB agent catalog and lifecycle in the standalone wizard.",
  "task_revision": 7,
  "title": "Authenticated agent wizard integration",
  "updated_at": "2026-09-15T16:22:09+00:00",
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
