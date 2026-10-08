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
  "task_revision": 21,
  "title": "Replace wizard free-form setup with bounded controls",
  "updated_at": "2026-10-08T07:50:04+00:00",
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

- 2026-10-08T07:38:06+00:00: Recorded command exit 0; command argv SHA-256
  87f33877f264dec5ec2991d95b1cc148fcd06c3f576e0c0118e60b27da0861a9.

- 2026-10-08T07:38:40+00:00: Recorded command exit 0; command argv SHA-256
  c275f5116a3adf17485ce02f6dfe9a874493e08a16b8b863d6cc0cc97aa45576.

- 2026-10-08T07:38:52+00:00: Recorded command exit 0; command argv SHA-256
  e83eb7cb291dae8668d2cf8f01aa77793881d41749856c2acd560b147001189f.

- 2026-10-08T07:42:32+00:00: Recorded command exit 1; command argv SHA-256
  22652158b656ead6aaee2f7d7f9c9602c3302c37b733b355be38a03406e9dc43.

- 2026-10-08T07:42:55+00:00: Recorded command exit 101; command argv SHA-256
  c84d1f6490263df738a2d6da24d05781d69e97c43e1da7653ae29f084d1251a1.

- 2026-10-08T07:45:03+00:00: Recorded command exit 0; command argv SHA-256
  ac3faf706b289f1ad357b241f63b4ceeec28fcefae13cb317fea7751f0f4f5d6.

- 2026-10-08T07:45:18+00:00: Recorded command exit 0; command argv SHA-256
  d23ab5b66a75e7a19903d695bebab773b39fae588d187c879c9f0ad8cbbde602.

- 2026-10-08T07:45:31+00:00: Recorded command exit 0; command argv SHA-256
  b224f58a36ccb79aa283e01dc348b9236f28bb0bfdcd6ee9d7f2fe64c1f21e30.

- 2026-10-08T07:46:27+00:00: Recorded command exit 0; command argv SHA-256
  a71d7cf2d673427d253074b45190b28836b2647a35d33d051fed592b02cb3ddd.

- 2026-10-08T07:46:41+00:00: Recorded command exit 0; command argv SHA-256
  59df26fc642ff0620686eb5be625d4738d4df0bc343bf0c53ced14d2eac22f73.

- 2026-10-08T07:47:00+00:00: Recorded command exit 0; command argv SHA-256
  32306c075293bfdb15c2c3df740a2df1d35d8aa5c717baedb0433d91481f21c2.

- 2026-10-08T07:48:12+00:00: Recorded command exit 0; command argv SHA-256
  a71d7cf2d673427d253074b45190b28836b2647a35d33d051fed592b02cb3ddd.

- 2026-10-08T07:48:43+00:00: Recorded command exit 101; command argv SHA-256
  0cdf8ddcb8357c805e05e0b5a1694ec429e3aa0f2ee3801162365304d0afd9d6.

- 2026-10-08T07:49:27+00:00: Recorded command exit 0; command argv SHA-256
  a71d7cf2d673427d253074b45190b28836b2647a35d33d051fed592b02cb3ddd.

- 2026-10-08T07:49:47+00:00: Recorded command exit 0; command argv SHA-256
  1960dffd7b3a20506f6b0055896a51f8d5466f664b7626f762241318670fe7aa.

- 2026-10-08T07:50:04+00:00: Recorded command exit 0; command argv SHA-256
  2b7b832dc3a49e845eee4c3d8d7fe5471ffd948e2854cca2ee694afb54f653d0.
