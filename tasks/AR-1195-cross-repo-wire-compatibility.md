---
{
  "branch": "feature/ar-1195-cross-repo-wire-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1192"],
  "id": "AR-1195",
  "next_action": "Align the standalone adapter with ASB v1.4/v1.5 canonical fixtures and run exact-head interoperability tests.",
  "owner": "",
  "plan": "../plans/AR-1195.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Prove asb-tui consumes the exact authenticated ASB catalog and lifecycle wire contracts.",
  "task_revision": 1,
  "title": "Cross-repository wire compatibility",
  "updated_at": "2026-09-15T07:45:00+00:00",
  "worktree_key": "asb-tui-cross-repo-wire-compatibility"
}
---

Replace any independently invented envelope or field model with an exact adapter for ASB's
authenticated JSON-RPC v1.4 catalog and v1.5 lifecycle responses. Preserve canonical digests,
numeric generations, target/libc metadata, closed enums, operation IDs and idempotency bindings.
Keep the UI state machine renderer-neutral and fail closed on schema, digest, identity or version
mismatch.
