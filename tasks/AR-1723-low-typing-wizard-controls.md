---
{
  "id": "AR-1723",
  "title": "Replace wizard free-form setup with bounded controls",
  "priority": "P0",
  "depends_on": [
    "AR-1668",
    "AR-1707",
    "AR-1720"
  ],
  "plan": "../plans/AR-1723-low-typing-wizard-controls.md",
  "summary": "Make the supported fresh-user wizard path use bounded selections and safe defaults instead of free-form configuration, credential-reference, recording-mode, and replay-policy entry.",
  "status": "planned",
  "next_action": "Promote immediately; implement bounded controls, formal-model and help parity, and an authoritative zero-free-form action-count regression, then requalify AR-1597.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 1,
  "schema_version": 1,
  "updated_at": "2026-10-08T07:35:00+00:00",
  "branch": "",
  "worktree_key": ""
}
---

AR-1597 proved that the functionally complete authoritative wizard route still
requires 132 key events, including 122 free-form characters across
configuration/default, credential reference, recording mode, and replay
policy. Replace those four supported-path text-entry steps with bounded,
contextual controls and safe development defaults. The ordinary supported
happy path must require zero free-form characters and no documentation lookup.

Preserve an explicit advanced/custom route only where the underlying ASB
contract supports it; it must not be required for the supported qualification
journey. Raw credentials remain outside TUI state. Missing development
authentication, signatures, and key management remain visible warnings and
never block local or deterministic qualification.
