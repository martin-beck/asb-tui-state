---
{
  "branch": "feature/ar-1321-credential-helper-bridge",
  "checkpoint_commit": "13dd5fa21d02e66c1b410f342cacb5ea70b8d3b3",
  "claim_expires": "",
  "depends_on": ["AR-1317"],
  "id": "AR-1321",
  "next_action": "Continue with AR-1323 for negotiated runner-owned helper invocation; PR #134 merged the strict digest-only receipt codec and PR #136 now projects runner-authored auth status before configuration apply.",
  "owner": "",
  "plan": "../plans/AR-1321.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Connect the setup wizard to an approved local credential helper without raw-key transport.",
  "task_revision": 4,
  "title": "Credential-helper bridge for setup wizard",
  "updated_at": "2026-09-21T02:52:00+00:00",
  "worktree_key": "asb-tui-ar-1321-credential-helper-bridge"
}
---

AR-1317 now documents the secure enrollment handoff and the typed transport
already supports digest-only enrollment/status/rotation/revocation. This AR
owns the missing user-facing bridge to an approved local helper/keychain,
including failure, cancellation, rotation, revocation, and restart behavior.
