---
{
  "branch": "upgrade/ar-1730-coordinator-v0.4.0-release",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1730",
  "next_action": "Promote and claim after state reconciliation; verify upstream v0.4.0 commit/tree and lightweight-tag provenance, then synchronize the exact release through the official vendor path in an isolated state worktree.",
  "owner": "",
  "plan": "../plans/AR-1730-coordinator-v040-release-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1730.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Adopt the exact Agent Workflow Coordinator v0.4.0 release and qualify ASB-TUI state compatibility without patching vendored bytes or weakening provenance gates.",
  "task_revision": 1,
  "title": "Coordinator v0.4.0 release vendor for ASB-TUI compatibility",
  "updated_at": "2026-10-09T00:00:00+00:00",
  "worktree_key": ""
}
---

The ASB-TUI state repository currently vendors Coordinator development commit
`e863b57edc7f7a21b2aff2c7b45ce226e12637d2`. Upstream now exposes the exact
`v0.4.0` release at commit `712b36ea3d188237cbe8104e70d905094f93a96b`, tree
`c496306050a805111f89b3f7bc4cfb0910f27535`. The remote tag is lightweight;
this AR records that limitation and does not claim an annotated tag signature.

This AR owns only the ASB-TUI state vendor and downstream compatibility. It must
preserve the project binding, Git backend, task lifecycle, privacy policy,
generated views, and source-only product boundary. No ASB product/state or
unrelated repository may be changed.
