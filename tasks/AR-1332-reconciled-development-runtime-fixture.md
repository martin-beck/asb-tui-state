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
  "status": "done",
  "summary": "Provide a reconciled disposable control-runtime fixture for AR-1323.",
  "task_revision": 4,
  "title": "Reconciled development control-runtime fixture",
  "updated_at": "2026-09-29T10:19:58+00:00",
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

- 2026-09-29T10:01:41+00:00: Promoted immediately by user authorization. Dependency direction
  corrected: AR-1332 is the repair prerequisite for AR-1323; work remains confined to
  asb-tui-compatible fixture/harness and state evidence.

- 2026-09-29T10:01:43+00:00: Claimed by tui-ar1332-repair-20260929.

- 2026-09-29T10:19:58+00:00: Completed in asb-tui PR #146, merged at
  95abcac67d0516aa2953cff280e6af0b99ee758d; deterministic typed reconciliation and reconnect harness
  passed local and hosted gates. Live runtime reconciliation remains external ASB contract.
