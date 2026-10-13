---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T07:29:52+00:00",
  "depends_on": [],
  "id": "AR-1737",
  "next_action": "Reproduce the exact ASB inherited-fd/PTY qualification against current asb-tui main, repair readiness-to-offline-run-control dispatch, and publish a reviewed PR with terminal-success CI.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-asb-tui-ar1737-offline-dispatch-20261013",
  "plan": "../plans/AR-1737-cross-repo-offline-run-control-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1737.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1737.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the current-main TUI readiness path so an inherited-fd PTY qualification dispatches the offline default run-control action after readiness.",
  "task_revision": 42,
  "title": "Repair offline run-control dispatch after TUI readiness",
  "updated_at": "2026-10-13T04:43:25+00:00",
  "worktree_key": ""
}
---

This AR owns the asb-tui side of the cross-repository qualification failure
reported by ASB PR #627. The current asb-tui main binary reaches readiness in
the inherited-file-descriptor PTY journey, but the offline default Run Control
action is not dispatched and the paired test fails at `tui.rs:6127`.

The repair must preserve the PTY, inherited-fd, source/binary digest, cleanup,
timeout, and fail-closed assertions. Do not fix this by pinning an obsolete
TUI revision, skipping the journey, relaxing timing, or changing ASB metadata.
Record only privacy-safe failure and qualification evidence.

- 2026-10-13: Created from ASB PR #627's repeated hosted failure against
  current asb-tui main (`486d24709d9045d8e4e2d91221db3a754d2fe3b6`).

- 2026-10-13T04:29:50+00:00: User prioritized the P0 current-main inherited-fd PTY
  readiness-to-offline Run Control repair.

- 2026-10-13T04:29:52+00:00: Claimed by codex-asb-tui-ar1737-offline-dispatch-20261013.

- 2026-10-13T04:30:58+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-10-13T04:31:11+00:00: Recorded command exit 0; command argv SHA-256
  4681f6e72914551b68091f3737eb96bf0a83e08e3350fdc071207054d12ed293.

- 2026-10-13T04:31:22+00:00: Recorded command exit 0; command argv SHA-256
  46de9ff749313683d7ffb858de9a4c2225a8f171108b9ad18c1bd62a5434dc14.

- 2026-10-13T04:31:34+00:00: Recorded command exit 0; command argv SHA-256
  4fcc6db0296ea752a1f3e784b4d4d396cab0bcd22f2053a42beb1ed95e279f7d.

- 2026-10-13T04:31:47+00:00: Recorded command exit 0; command argv SHA-256
  633a3e8980f48c382243687e33c31767056bf5ab5772658cbb1898535ae85f01.

- 2026-10-13T04:32:01+00:00: Recorded command exit 0; command argv SHA-256
  23bd3b102b0d507152cea69896acdee445c442c87a35609fda598b5ee21f9725.

- 2026-10-13T04:32:12+00:00: Recorded command exit 0; command argv SHA-256
  60ec3ee5a7347ba20393a9a27aa6701c52c126c3574b61eab4e160f7df686f3e.

- 2026-10-13T04:32:31+00:00: Recorded command exit 0; command argv SHA-256
  745f60e922c6345f9fe10cac5dc930c0486eccf510b460d44e61cb6ccda27c76.

- 2026-10-13T04:32:46+00:00: Recorded command exit 0; command argv SHA-256
  5ed8ebee8ea02187a404a4c8c2ce894af76a99e63a3e61891ad9da05f571e717.

- 2026-10-13T04:32:57+00:00: Recorded command exit 0; command argv SHA-256
  edac6de9b011864d4541b190e293b251df952cf7913db1e6192dfbef2cdf48a2.

- 2026-10-13T04:33:10+00:00: Recorded command exit 0; command argv SHA-256
  7a9c6be653aecd6a8f6617080fee1133bb7e592d4d728b735ed4303ac841bf7c.

- 2026-10-13T04:33:22+00:00: Recorded command exit 0; command argv SHA-256
  0f8e460aa29e4a680ec28a708fe549eef116566402faf8d44cf890b7d1aab6f5.

- 2026-10-13T04:33:33+00:00: Recorded command exit 0; command argv SHA-256
  54ea752572997fd0cd775aca4aebba38ba61f1eb7aca757fb2d048396d735a3c.

- 2026-10-13T04:33:44+00:00: Recorded command exit 0; command argv SHA-256
  a199ae65535184918c273f3130065d6d9704503e576effb7f0907d107e11d3ac.

- 2026-10-13T04:33:59+00:00: Recorded command exit 0; command argv SHA-256
  b7567c9f6392d9c1d01887e480f258e62a4a2c2115dfbb6657b48226a530ac64.

- 2026-10-13T04:34:11+00:00: Recorded command exit 0; command argv SHA-256
  b66fa6dcac39695b7919aba4fb78603a837a9c4350dd44b7a13c3ffd7328aa95.

- 2026-10-13T04:34:24+00:00: Recorded command exit 0; command argv SHA-256
  18183d984d433e6f272b2c05e0c34b90ec4333bfd68d7ad926191dcaba676b24.

- 2026-10-13T04:35:03+00:00: Recorded command exit 0; command argv SHA-256
  e38c0063c3101a1b88d25c35e7778154f7f3ba81040a4bec09abfab2ac9d71d5.

- 2026-10-13T04:35:48+00:00: Recorded command exit 101; command argv SHA-256
  e94cf6dc47102fc274c067cb85dde71a4f9c59beaceeb0bc9dc3b54ac8fc6058.

- 2026-10-13T04:36:18+00:00: Recorded command exit 0; command argv SHA-256
  7659c258644e273af778edd07f3e6bcb97819c28ce14b869a7abaeb9bfab26b7.

- 2026-10-13T04:36:28+00:00: Recorded command exit 0; command argv SHA-256
  a17b1b1e66d195d6b0286003d30db4b51fe4510b75b1267c4f3c2b767e773ec3.

- 2026-10-13T04:36:39+00:00: Recorded command exit 0; command argv SHA-256
  ccbbd746bc0f67b1ef4980854d4e1af287f4d97d9340c8d12d6912bdfa625de8.

- 2026-10-13T04:36:57+00:00: Recorded command exit 0; command argv SHA-256
  d57c3728fdc06f9b774fe26b70d0900b96dc710a49d484f1549f95bccdd63e9a.

- 2026-10-13T04:37:20+00:00: Recorded command exit 0; command argv SHA-256
  75ba4d1920f9de49df4fbc9cf50624e3dba0366f13680af3c496fb4cfe8bdba6.

- 2026-10-13T04:37:38+00:00: Recorded command exit 0; command argv SHA-256
  4322860e86d29d48f99b3d3b67de222c6b08a98b8068db2bb0bb6cabb475ad79.

- 2026-10-13T04:37:56+00:00: Recorded command exit 0; command argv SHA-256
  5d31320e312c6de146d7a6cfaba9e0f2fb2579d4cfcfbf440a153c4f4d4d6e83.

- 2026-10-13T04:38:06+00:00: Recorded command exit 0; command argv SHA-256
  182ed04904be79f6386b756aba83353401c732b0b8ab65987d96ca3fd985fab7.

- 2026-10-13T04:38:37+00:00: Recorded command exit 0; command argv SHA-256
  7da0a3b3d7c4211ef43e221b7726bb28bc3592f4562fab1d8618093da06299c1.

- 2026-10-13T04:38:49+00:00: Recorded command exit 0; command argv SHA-256
  889e08b53a0bb083a3d2d395d518ef126bd26f52b3720b5b0dce18f20cdb5356.

- 2026-10-13T04:39:11+00:00: Recorded command exit 0; command argv SHA-256
  763e9b892cab52967134518f172b98097ebcdade0f780854e375accdf017462f.

- 2026-10-13T04:39:56+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-13T04:40:29+00:00: Recorded command exit 0; command argv SHA-256
  c1611b238f1cfdca29fe7db38fef749ba77767ba1ed17d6d4cbd2fe2cc28f46c.

- 2026-10-13T04:41:14+00:00: Recorded command exit 0; command argv SHA-256
  0f2b207a431a0043c042c0a039ab37395f9b4237a9bad31ef56af3d011d689b8.

- 2026-10-13T04:41:37+00:00: Recorded command exit 0; command argv SHA-256
  de43e3c521573c3a53b5ac7c63a9d1ab88e61bbe65a64e4324275b949e61f5b0.

- 2026-10-13T04:41:57+00:00: Recorded command exit 2; command argv SHA-256
  0635b703c368c4bed80d712a35bc3f3c5ccf4fd99fbd8373710f47dffb8317df.

- 2026-10-13T04:42:07+00:00: Recorded command exit 0; command argv SHA-256
  de8d0fa503578eb2a4b5b8d740410034b588ae603a01b221ccba72c1f1a596d3.

- 2026-10-13T04:42:56+00:00: Recorded command exit 0; command argv SHA-256
  2dcd4328cb1588ed5ef179c17405576c0f5b2d234a53281d9513e19e9f03cd5f.

- 2026-10-13T04:43:14+00:00: Recorded command exit 0; command argv SHA-256
  5c4d7ed941e47bce9e3a8f2789e209971f62bce44e3b325561f0fc65823d9c50.

- 2026-10-13T04:43:25+00:00: Recorded command exit 0; command argv SHA-256
  9cd78a804ce7bea7869ca5d72ba4b57c66170f6ea700121d525b8e4540a7112c.
