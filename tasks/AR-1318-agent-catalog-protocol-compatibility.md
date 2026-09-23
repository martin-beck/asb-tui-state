---
{
  "branch": "feature/ar-1318-agent-catalog-protocol-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1318",
  "next_action": "Update the TUI agent-catalog codec/projection for ASB's signer, SBOM, license and target provenance fields, then publish exact fixture evidence.",
  "owner": "",
  "plan": "../plans/AR-1318.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Keep asb-tui agent-catalog decoding compatible with the current ASB authenticated schema.",
  "task_revision": 3,
  "title": "Agent catalog protocol compatibility",
  "updated_at": "2026-09-23T23:51:45+00:00",
  "worktree_key": "asb-tui-ar-1318-agent-catalog-protocol-compatibility"
}
---

The TUI currently rejects the current ASB catalog's additional required
provenance fields because its codec uses strict unknown-field validation. Keep
the contract fail-closed while making the versions and generated fixtures agree.

- 2026-09-23T23:51:37+00:00: Claimed by codex-asb-tui-reconcile-20260924.

- 2026-09-23T23:51:45+00:00: Verified PR #131 (feature/ar-1318-agent-catalog-compat) is merged with
  successful repository quality, supply-chain, privacy, and AWQ checks. Current asb-tui main
  contains signer, SBOM, license, target, availability validation and projection coverage; no
  duplicate implementation required.
