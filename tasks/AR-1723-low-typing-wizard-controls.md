---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T11:37:35+00:00",
  "depends_on": [
    "AR-1668",
    "AR-1707",
    "AR-1720"
  ],
  "id": "AR-1723",
  "next_action": "Promote immediately; implement bounded controls, formal-model and help parity, and an authoritative zero-free-form action-count regression, then requalify AR-1597.",
  "owner": "codex-ar1723-low-typing-20261008",
  "plan": "../plans/AR-1723-low-typing-wizard-controls.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the supported fresh-user wizard path use bounded selections and safe defaults instead of free-form configuration, credential-reference, recording-mode, and replay-policy entry.",
  "task_revision": 5,
  "title": "Replace wizard free-form setup with bounded controls",
  "updated_at": "2026-10-08T07:37:54+00:00",
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

- 2026-10-08T07:36:52+00:00: Dependencies AR-1668, AR-1707, and AR-1720 are done; independently
  reviewed AR-1597 evidence requires bounded controls and an action-count regression.

- 2026-10-08T07:37:35+00:00: Claimed by codex-ar1723-low-typing-20261008.

- 2026-10-08T07:37:42+00:00: Recorded command exit 0; command argv SHA-256
  9d4fb1971e8537df234621ae98ef5afd37bdcac53f8a96b0683427969d8df36e.

- 2026-10-08T07:37:54+00:00: Recorded command exit 0; command argv SHA-256
  5d90820bc527fbfeac5be9843bcfa376321a569c12dc3ce3287529f5fa9081cd.
