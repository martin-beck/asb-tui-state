---
{
  "branch": "feature/ar-1332-reconciled-development-runtime-fixture",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1332",
  "next_action": "Implement the asb-tui-compatible qualification harness and record successful v1.10 digest-only AuthStatus evidence; this repair unblocks AR-1323.",
  "owner": "",
  "plan": "../plans/AR-1332.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide a reconciled disposable control-runtime fixture for AR-1323.",
  "task_revision": 1,
  "title": "Reconciled development control-runtime fixture",
  "updated_at": "2026-09-29T09:50:00+00:00",
  "worktree_key": "asb-tui-ar-1332-reconciled-development-runtime-fixture"
}
---

AR-1323 proved the asb-tui provisioning handoff, v1.10 negotiation, digest-only
enrollment, and allowlisted helper execution. The disposable runtime then
returned typed `runner reconciliation is required` during the helper mutation.
This AR owns the qualification fixture and recovery contract needed to remove
that blocker without requiring production authorization.

- The runtime-side catalog/reconciliation repair is an external ASB contract;
  this task must not modify the ASB repository.
- The asb-tui side may add only a compatible fixture harness, typed recovery
  assertions, and evidence required by the development qualification.
- Raw helper output, credentials, production claims, and authorization tokens
  are prohibited from fixture artifacts and logs.
