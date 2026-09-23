---
{
  "branch": "feature/ar-1318-agent-catalog-protocol-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T00:21:37+00:00",
  "depends_on": [],
  "id": "AR-1318",
  "next_action": "Update the TUI agent-catalog codec/projection for ASB's signer, SBOM, license and target provenance fields, then publish exact fixture evidence.",
  "owner": "codex-asb-tui-reconcile-20260924",
  "plan": "../plans/AR-1318.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Keep asb-tui agent-catalog decoding compatible with the current ASB authenticated schema.",
  "task_revision": 2,
  "title": "Agent catalog protocol compatibility",
  "updated_at": "2026-09-23T23:51:37+00:00",
  "worktree_key": "asb-tui-ar-1318-agent-catalog-protocol-compatibility"
}
---

The TUI currently rejects the current ASB catalog's additional required
provenance fields because its codec uses strict unknown-field validation. Keep
the contract fail-closed while making the versions and generated fixtures agree.

- 2026-09-23T23:51:37+00:00: Claimed by codex-asb-tui-reconcile-20260924.
