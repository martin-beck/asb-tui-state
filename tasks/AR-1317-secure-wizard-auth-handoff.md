---
{
  "branch": "feature/ar-1317-secure-wizard-auth-handoff",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1192",
    "AR-1197",
    "AR-1228",
    "AR-1229"
  ],
  "id": "AR-1317",
  "next_action": "Continue with AR-1321: connect the documented secure handoff to an approved local credential helper and typed enrollment/status projection.",
  "owner": "",
  "plan": "../plans/AR-1317.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Complete secure API-key enrollment UX in the setup wizard without raw-key transport.",
  "task_revision": 4,
  "title": "Secure setup-wizard authentication handoff",
  "updated_at": "2026-09-21T03:50:28+00:00",
  "worktree_key": "asb-tui-ar-1317-secure-wizard-auth-handoff"
}
---

The current wizard accepts only a credential-reference digest and the transport
already exposes typed auth enrollment methods, but no user-facing enrollment
handoff exists. Implement the linked plan after the live catalog dependency is
available; preserve the credential-free control boundary.

- 2026-09-21T03:50:11+00:00: Dependencies AR-1192 and AR-1197 stale blocks reconciled done after ASB
  AR-1316 merge; proceed with secure handoff reconciliation.

- 2026-09-21T03:50:14+00:00: Claimed by codex-ar1317.

- 2026-09-21T03:50:28+00:00: Reconciled secure wizard auth handoff: merged TUI PRs #134/#136 provide
  digest-only helper receipt transport and runner-auth status projection; ASB AR-1324 now adds
  negotiated runner-owned helper invocation. Existing formal and hosted gates are green.
