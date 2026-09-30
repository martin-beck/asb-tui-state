---
{
  "branch": "feature/ar-1200-asb-router-client",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T07:46:36+00:00",
  "depends_on": [
    "AR-1195"
  ],
  "id": "AR-1200",
  "next_action": "Promote and implement the development router client against the local contract fixtures; qualify install/status/upgrade/remove/launch with warning-only development fallback.",
  "observed_branch": "feature/ar-1200-asb-router-client",
  "observed_dirty": 0,
  "observed_head": "92a458a0fe88d2c935d3c8854450c258957d03f9",
  "owner": "tui-ar1200-dev-20261001",
  "plan": "../plans/AR-1200.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt the ASB development router from the standalone asb-tui lifecycle and UI.",
  "task_revision": 13,
  "title": "ASB development router client adoption",
  "updated_at": "2026-09-30T05:52:10+00:00",
  "worktree_key": "asb-tui-ar-1200"
}
---

This task owns the TUI-side development client and may use local contract fixtures. Actual UI
application and rendering remain here; ASB owns only the backend/control route. Production
authentication and remote trust are explicitly outside this development AR.

- 2026-09-29T09:37:29+00:00: Local AR-1195 dependency is done; the former external authenticated-router
  gate is removed for the development profile. Production trust remains a separate future concern.

- 2026-09-29T09:37:52+00:00: Claimed by tui-ar1200-gate-audit-20260929.

- 2026-09-29T09:38:50+00:00: External paired dependencies remain unmet; released without product
  work and restored planned gate.

- 2026-09-30T05:46:33+00:00: Development-only gate removal is committed at 3c6b6fd; promote local
  fixture-backed router implementation. Production trust remains explicitly out of scope.

- 2026-09-30T05:46:36+00:00: Claimed by tui-ar1200-dev-20261001.

- 2026-09-30T05:47:00+00:00: Recorded command exit 0; command argv SHA-256
  422c85b7e92211a0c7686a84ca032cfadd21d841603e6b6b8ad343114f82ce53.

- 2026-09-30T05:51:36+00:00: Recorded command exit 128; command argv SHA-256
  f8f66f1cdb092d9437f5dc3d8d9c36ac8f14eb211f9b1b0c7ff497288f73e2d5.

- 2026-09-30T05:51:53+00:00: Recorded command exit 0; command argv SHA-256
  9141c857110f20e25a05d603ad483772a692ddbe2c8eff071a92b180b82e9f79.

- 2026-09-30T05:52:10+00:00: Recorded command exit 0; command argv SHA-256
  6b54db36de03a9cdd089662a556efd015787144e9e8446ed09602656b4e59a5c.
