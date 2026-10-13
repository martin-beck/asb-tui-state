---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T07:29:52+00:00",
  "depends_on": [],
  "id": "AR-1737",
  "next_action": "Obtain independent exact-head approval and terminal hosted checks for repair PR #305; do not merge.",
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
  "task_revision": 169,
  "title": "Repair offline run-control dispatch after TUI readiness",
  "updated_at": "2026-10-13T05:36:42+00:00",
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

- 2026-10-13T04:44:03+00:00: Recorded command exit 0; command argv SHA-256
  9155475f01d87ac1ceedcb4a457f64ca0abfebec794e9a42066050050797b7c1.

- 2026-10-13T04:44:18+00:00: Recorded command exit 0; command argv SHA-256
  4d771aa8746a45a7bb4b22b8b0b318c1611abf048cca86a92eeea385af9446a1.

- 2026-10-13T04:44:30+00:00: Recorded command exit 0; command argv SHA-256
  ff78fe79f459d150be8056b967a14154028255eba8f9170df96805a340c7666f.

- 2026-10-13T04:44:41+00:00: Recorded command exit 0; command argv SHA-256
  66c8f6badd7fc9334dc603012cec250c829372ee73a3470c1b45a60931c45176.

- 2026-10-13T04:45:05+00:00: Recorded command exit 101; command argv SHA-256
  1220cdd7e4f4a2857ef02d8fd16f23e7b89dde6f67ba8322e587d3d6924a683e.

- 2026-10-13T04:45:18+00:00: Recorded command exit 0; command argv SHA-256
  ad8544f690c7e4b6ed747dec68ef4099a718fbb8324923a58a8d8795e2016026.

- 2026-10-13T04:45:36+00:00: Recorded command exit 101; command argv SHA-256
  092f64ac4609187b44e1dc88e5da8438f04530ff6b6b733af05fd5afb3eb8da1.

- 2026-10-13T04:45:54+00:00: Recorded command exit 0; command argv SHA-256
  325ace20660c3f13ca6fd288d80723e8993e747ee67643c94b942c157baa0831.

- 2026-10-13T04:46:10+00:00: Recorded command exit 0; command argv SHA-256
  979864db0bcd4eed66ed4f1c9d7f0ea28a32530929a1bd0487a79b0ff0d49268.

- 2026-10-13T04:46:24+00:00: Recorded command exit 0; command argv SHA-256
  9a8ee8183d286098211a0db18ad18f8c4909b0d9cee0b6de19e05e391d72ffd3.

- 2026-10-13T04:46:40+00:00: Recorded command exit 0; command argv SHA-256
  0109515cebc7e9209253ecfd46e6bfa9c25de29f2ef43b99276f7add05147380.

- 2026-10-13T04:47:06+00:00: Recorded command exit 0; command argv SHA-256
  478bba8bef827ffb8cbf0adf58b8d96ca3e08be0d4466bb042bd118577888cbb.

- 2026-10-13T04:47:21+00:00: Recorded command exit 101; command argv SHA-256
  c3674f020c794212282d411c56c09cef7f6bb82ba24a17f45004053b5bf312d2.

- 2026-10-13T04:47:29+00:00: Recorded command exit 0; command argv SHA-256
  31e098a650b19c1c709547ec2376f8ce329f145d74f535f32e51af3507d381b5.

- 2026-10-13T04:47:38+00:00: Recorded command exit 0; command argv SHA-256
  d19064016e6242bd55c51589db4c7dbc703f46b1c0a08939f4f1b096221b1299.

- 2026-10-13T04:47:51+00:00: Recorded command exit 101; command argv SHA-256
  a14b2606781b61f37d6070282d315ead9ba44be9e9421a03c7f6efc515f16365.

- 2026-10-13T04:48:00+00:00: Recorded command exit 0; command argv SHA-256
  06ec773b4553d2db3ea070b5ad31b0c31cc8dfde8f97ab76a63383b5eef72cc8.

- 2026-10-13T04:48:16+00:00: Recorded command exit 0; command argv SHA-256
  15e8d345ecdac4db66b7d66886e14c49abcd89a373066269480a7530059a0827.

- 2026-10-13T04:48:54+00:00: Reproduced ASB PR #627 exact inherited-fd/PTY failure against asb-tui
  main cf45a645887a8f8713b72f7f717b08fc8786a9ec tree 495de1c8ba2bd2dfa65b591aac425fa1fd1ec15b and
  binary digest 9d000d2810c84f9ecf08efaffc138263c161de2835eead1012b624b05ece77a4. Root cause is
  authoritative measure bulk-selection key drift from lowercase a to uppercase A: the paired PTY
  sends lowercase a, leaving scope empty and the next recording action terminating the frontend.
  Restoring lowercase a plus in-session fail-closed dispatcher preparation makes the unchanged
  cross-repo test pass; focused readiness, premature, malformed, stale, unavailable, formal-model,
  source-parity, and visual-parity tests are green.

- 2026-10-13T04:49:01+00:00: Recorded command exit 0; command argv SHA-256
  afcb2f6ab0b42204924e4bd362546f3dfd38cae8735337f22bfd2f1a73502e8b.

- 2026-10-13T04:49:10+00:00: Recorded command exit 0; command argv SHA-256
  c165f40579e39e82cf093b4414553eef476cdd38d115d9473994da2501d861b5.

- 2026-10-13T04:49:33+00:00: Recorded command exit 0; command argv SHA-256
  948484f80deee1407d6fb904518f124abb3facc91a01238945b5cea3ec754955.

- 2026-10-13T04:49:46+00:00: Recorded command exit 0; command argv SHA-256
  8e658a7378e8f05c996b7c6beb05af87a4fd623e3305a7338129b428e45d1a24.

- 2026-10-13T04:49:55+00:00: Recorded command exit 0; command argv SHA-256
  6ec151b925e47d27ba338b2ac9b7a1ab7203a5285863a619d6c83aa85b815de0.

- 2026-10-13T04:50:02+00:00: Recorded command exit 0; command argv SHA-256
  918c81e493bbee42c7bce20b4d0bb1b0d6897b567df3b9d0ea98eb19855a74fb.

- 2026-10-13T04:51:57+00:00: Recorded command exit 101; command argv SHA-256
  a8845e3e7491d5283783621661e1da10616a339ef3958adc38dcf5df92d471a9.

- 2026-10-13T04:52:03+00:00: Recorded command exit 0; command argv SHA-256
  a8c71030700950a75d896e89fa056ea1f0f85b8773cf4f99949bfdbe934df384.

- 2026-10-13T04:52:16+00:00: Recorded command exit 0; command argv SHA-256
  786d2db82cf59db0f178a8401e652030b61c2a598943c57cad58e5aec4d43bab.

- 2026-10-13T04:52:24+00:00: Recorded command exit 0; command argv SHA-256
  ac2ced2ba8334751dcd32947fab3e735e6e15afd29acb4e8308ce87a6bffec0d.

- 2026-10-13T04:54:19+00:00: Recorded command exit 0; command argv SHA-256
  a8845e3e7491d5283783621661e1da10616a339ef3958adc38dcf5df92d471a9.

- 2026-10-13T04:55:31+00:00: Recorded command exit 1; command argv SHA-256
  22f097d9d157731a6c8a08bc714f21d86a1016e84600092e6787310400cd950a.

- 2026-10-13T04:55:40+00:00: Recorded command exit 0; command argv SHA-256
  ab4578c687ee8ad1b38058d1c9537a14c16b0d4abf87a1ab46c41152c29bc927.

- 2026-10-13T04:55:57+00:00: Recorded command exit 0; command argv SHA-256
  8a964ca60275a9b9556c008635a76c93f8a25046eff6491b73a4bb82e9b6ed48.

- 2026-10-13T04:56:07+00:00: Recorded command exit 0; command argv SHA-256
  4f2e2a2986f0c4a4dce13de81609bd9c27868157844d2847ee698d2ef187a43e.

- 2026-10-13T04:56:22+00:00: Recorded command exit 0; command argv SHA-256
  eb94c32ac4d4fc198bea02fc30d7b194fc27ca94be2c5610eb0944c6c7ab7483.

- 2026-10-13T04:56:47+00:00: Recorded command exit 0; command argv SHA-256
  0453db489630f734029bbbb8c582fc8432ae5627fb481817a2f4bf61a6e6f045.

- 2026-10-13T04:56:58+00:00: Recorded command exit 0; command argv SHA-256
  cc0cd88bcdecc00d005c17f2e79e9006c3f5ca54559730b6ecf2681a3187d7eb.

- 2026-10-13T04:57:09+00:00: Recorded command exit 1; command argv SHA-256
  83afdba60ca0e1e080fd02cc416254e22d7b767c2d8a852faceb177be2ba49ed.

- 2026-10-13T04:57:23+00:00: Recorded command exit 0; command argv SHA-256
  3b1c32311c8adfcc7b88b0b62902730653a202f119e3609013ccf86b7fedc8dc.

- 2026-10-13T04:58:15+00:00: Recorded command exit 0; command argv SHA-256
  51326866fc7c9410c68c61243020afc9e377bfb76f9b365ae52e9c00068a8432.

- 2026-10-13T04:58:20+00:00: Recorded command exit 0; command argv SHA-256
  2d69b32d7ad083ab74a709517e086e70abc42faaeb8b326ead02e0b39e80f685.

- 2026-10-13T04:58:24+00:00: Recorded command exit 0; command argv SHA-256
  7a37aaf8481c7e9f16d14e4d2e172262f59a974ef65872c290b1fd5a0f346068.

- 2026-10-13T04:58:33+00:00: Recorded command exit 0; command argv SHA-256
  052d4ca52a11d3bc49181f09623c3c477040f9bcc1d00bbf2cf1215459672041.

- 2026-10-13T04:58:57+00:00: Recorded command exit 0; command argv SHA-256
  a82d36bd6d2a3f341336e3f8d0a7e1c618346872faa9a0d4d7ba22c079282b54.

- 2026-10-13T04:59:15+00:00: Recorded command exit 8; command argv SHA-256
  2fb6dc8925c790d11d3f5bf17d1856cd9a2cb5dad48d9a7e2a99f7d95425d59b.

- 2026-10-13T04:59:39+00:00: Published signed+DCO product candidate PR #304 at base
  cf45a645887a8f8713b72f7f717b08fc8786a9ec, head 85e35a62da8dc51f2b4f34d93f7fc581cd7d7204, tree
  7d69c5fd6c88a1efc7df8204b56a74573efb5403. Final release binary sha256
  9168d8885ebc04942c0507416bac0f8472c0584c926ea591850987d940c07d2f passed the exact unchanged ASB PR
  #627 inherited-fd/PT​​Y qualification 1/1 in 4.43s with no matching child remaining. Local full
  gates green; independent review assigned and hosted checks pending.

- 2026-10-13T04:59:45+00:00: Recorded command exit 8; command argv SHA-256
  2fb6dc8925c790d11d3f5bf17d1856cd9a2cb5dad48d9a7e2a99f7d95425d59b.

- 2026-10-13T05:03:43+00:00: Recorded command exit 0; command argv SHA-256
  0616787630b0dce656cfc3a71e2b37954ebf6e0c2c0ab904fcac691b9af5edf4.

- 2026-10-13T05:03:53+00:00: Recorded command exit 0; command argv SHA-256
  9bf3b805772cf65b06fd165e593f16b72625ad5324bfda1186bff9759333af13.

- 2026-10-13T05:04:06+00:00: Recorded command exit 0; command argv SHA-256
  9fa6888372c7b572dab6f2963eb76ea69d9da2e1de1f507fc5725d69a97eb2da.

- 2026-10-13T05:04:17+00:00: Recorded command exit 0; command argv SHA-256
  a3668c60ddda57d2a39ce4f5be82207096d3523f0f3c620cad86e01ecd965f92.

- 2026-10-13T05:04:34+00:00: Recorded command exit 0; command argv SHA-256
  a3652a780a507517c616bd606fdc3ba81b4ecf9aa18f73c0ab3fa97cf5442b69.

- 2026-10-13T05:05:08+00:00: Recorded command exit 0; command argv SHA-256
  522d3af9001edd6f3786f5b15b176f55efd3007e8291c098d50c98b03c7826ac.

- 2026-10-13T05:05:27+00:00: Recorded command exit 0; command argv SHA-256
  ea17a35faf76eb7c98dec5e2e64dee8f1df85841dc5539779e8583493f0dba4d.

- 2026-10-13T05:05:36+00:00: Recorded command exit 0; command argv SHA-256
  72a517a786aa40db673ccc763f085442e563beca397bbfa8d9e30141b377dbbc.

- 2026-10-13T05:05:47+00:00: Recorded command exit 0; command argv SHA-256
  ec26fa263276789a3e32092facc8dd781211fb7676e27db892cefa50a4a2e31f.

- 2026-10-13T05:06:50+00:00: Recorded command exit 0; command argv SHA-256
  870c124e6d98ab8f3a2d2cedcba41e97e0bba08e450ba1125a453f54b1445e8f.

- 2026-10-13T05:07:07+00:00: Recorded command exit 0; command argv SHA-256
  032547cd7a158d46e79f8fd4ecdbc8c0f5952e1c0b6f96e1586c9da1fb910c6e.

- 2026-10-13T05:07:17+00:00: Recorded command exit 0; command argv SHA-256
  5d96bfaf23e4a398eb258c6442436c2d3298198f9bb34fe5f790dcd2211e21b0.

- 2026-10-13T05:07:27+00:00: Recorded command exit 0; command argv SHA-256
  5e90b5626ed14c6f6c9f587e0033236134623ed0f83e9c9d5faf31d4b82f37c5.

- 2026-10-13T05:07:37+00:00: Recorded command exit 0; command argv SHA-256
  ba8043393b102ed4b23e295337a8701662c24e9e3d43658e621a3281230f2353.

- 2026-10-13T05:07:54+00:00: Recorded command exit 0; command argv SHA-256
  34f17fefe050bdb41f3be664a6d31681f2952231b6e2972f70ffbc19cc95e45c.

- 2026-10-13T05:08:08+00:00: Recorded command exit 0; command argv SHA-256
  011f085228a02e424eb077dd1b8a10c2729cf0e8f33a57c98f94e01983de6e08.

- 2026-10-13T05:08:30+00:00: Recorded command exit 1; command argv SHA-256
  036568990c38ed6b343fe2eeb7d7312bcf70c2029e24d2899ab01904f419a8e2.

- 2026-10-13T05:08:33+00:00: Recorded command exit 0; command argv SHA-256
  8340a1c25b5d6c5918291ba570650c7d1e87b929905d4e6352cca3472938db4a.

- 2026-10-13T05:08:45+00:00: Recorded command exit 0; command argv SHA-256
  db13e396740b06fe8d64e90e618fff4d78b2b6e40bb059f28d5c3c1bc430ca53.

- 2026-10-13T05:08:52+00:00: Recorded command exit 0; command argv SHA-256
  011f085228a02e424eb077dd1b8a10c2729cf0e8f33a57c98f94e01983de6e08.

- 2026-10-13T05:09:01+00:00: Recorded command exit 0; command argv SHA-256
  46a47ab822f84267d448054170d0e78b914c8f5229926b5048f72ec85980749e.

- 2026-10-13T05:09:10+00:00: Recorded command exit 0; command argv SHA-256
  656fc12b242c589b032ce5c631c4e155cf0c169590bbeb45375127cfe792f0dc.

- 2026-10-13T05:09:20+00:00: Recorded command exit 1; command argv SHA-256
  71161650aec1922624cbaee49ff6a30499fbfe0e8865c2f6270ebbcc81f2e5ea.

- 2026-10-13T05:09:43+00:00: Recorded command exit 0; command argv SHA-256
  011f085228a02e424eb077dd1b8a10c2729cf0e8f33a57c98f94e01983de6e08.

- 2026-10-13T05:09:52+00:00: Recorded command exit 0; command argv SHA-256
  9d6b28f31a7d05261ed318ed3e35974561498a0df58f97046f5639801a13d444.

- 2026-10-13T05:10:10+00:00: Recorded command exit 0; command argv SHA-256
  895193f684238133edf1ec0ed69061cc9d8830cafaff7ce947c29a98ce765f9a.

- 2026-10-13T05:10:19+00:00: Recorded command exit 0; command argv SHA-256
  9e66fce35a5c978d7db09058131e4467fe58fa8d1bbf85831e5184338e9ee18c.

- 2026-10-13T05:10:35+00:00: Recorded command exit 0; command argv SHA-256
  27ccca6946737af29e5c255ac5eff5e6cafbae56e2166696c23181664167dbe4.

- 2026-10-13T05:10:37+00:00: Recorded command exit 0; command argv SHA-256
  f25741a0bfc2a118355a7a4b40197d14e47bd4ed8d8b6da1103eade2201ea6d0.

- 2026-10-13T05:10:46+00:00: Recorded command exit 0; command argv SHA-256
  acd03dcce88131900494e3488586dca4733c94699201d47d513a3fa4a8027cc7.

- 2026-10-13T05:11:34+00:00: Recorded command exit 1; command argv SHA-256
  f8f0fd07e95107b0fbdf8d2fd0c86021d7085d4d4983fd60597e7ca16cda00f2.

- 2026-10-13T05:12:16+00:00: Recorded command exit 1; command argv SHA-256
  b84483e56c3548506b7c067adfb24245f89ff122fb38a7a6339ff10f328d97d7.

- 2026-10-13T05:12:40+00:00: Recorded command exit 0; command argv SHA-256
  0cac13f99eb760dd6ba9c3f397dcc80d213397f974903bba75ef76a0d2c14393.

- 2026-10-13T05:12:54+00:00: Recorded command exit 0; command argv SHA-256
  1bb34bba0176b506329c71ab9a6ae997c694e3ea40688d4838d8b5ee82d71116.

- 2026-10-13T05:13:18+00:00: Recorded command exit 0; command argv SHA-256
  7187f4a243ae5404d16dcd08e238062e97dcfeb0bb38701d55c243c271683ad9.

- 2026-10-13T05:15:37+00:00: Recorded command exit 0; command argv SHA-256
  089ed8afca7116bcfbf9c7317cae0f53a9f7dde0f7b4eb0e4c31440445666093.

- 2026-10-13T05:15:47+00:00: Recorded command exit 2; command argv SHA-256
  5580829ef71547f7d81b5aa45a59f5078d749c3ea19edc2898295cfdbf515695.

- 2026-10-13T05:15:56+00:00: Recorded command exit 0; command argv SHA-256
  09b0183928027245fd069d19fdb57cdc0e05d25f23663570e629580488240325.

- 2026-10-13T05:16:05+00:00: Recorded command exit 0; command argv SHA-256
  c1657c55c02e59578ccabebb1be9bfc033a80bfb48fd7df91919569f78ec5ab0.

- 2026-10-13T05:16:14+00:00: Recorded command exit 0; command argv SHA-256
  85cf5932d4d596fbabb13e41ee6a5a863a548914ae6b53c9c7376a7a000fee82.

- 2026-10-13T05:16:24+00:00: Recorded command exit 1; command argv SHA-256
  e027ee50ce8f8c0912cd2eb925ae07165bf1340562e92de229aebfbd2377ca82.

- 2026-10-13T05:16:32+00:00: Recorded command exit 0; command argv SHA-256
  17b981c4b34ba458c781a77f5dbc69eeb93b525948cad2f72add454ce9907bf6.

- 2026-10-13T05:16:50+00:00: Recorded command exit 0; command argv SHA-256
  543bfd9e78a541bf5d628f6ea167d146f1e0eee7804955e74542080575782fa1.

- 2026-10-13T05:17:11+00:00: Recorded command exit 0; command argv SHA-256
  1f8bb5a902b8a1b83ef70ebfc52346c9cfc098455409a1dede866a444d0c648a.

- 2026-10-13T05:17:37+00:00: Recorded command exit 101; command argv SHA-256
  302a9257bd50cc9aa360efb258b53642f798a534573f89b20330e69877541119.

- 2026-10-13T05:18:18+00:00: Recorded command exit 101; command argv SHA-256
  d24c5c30aaf23d70eeaad02ae33957211e2158b505abe94f8ddb8fcb74ab0415.

- 2026-10-13T05:18:39+00:00: Recorded command exit 0; command argv SHA-256
  eeba86362e1fcda807e5c4b2f695d3d1a9880867bd49c8734e3e8557588557b5.

- 2026-10-13T05:18:49+00:00: Recorded command exit 0; command argv SHA-256
  84f68d2999ab3f3475f993efd92f1a1b23e186a4a9aaf87a24a4f86a7d9e9136.

- 2026-10-13T05:19:14+00:00: Recorded command exit 0; command argv SHA-256
  be056020749506790073701be6e99cc570de74cd219381ed6cce6d1d380f5c68.

- 2026-10-13T05:19:29+00:00: Recorded command exit 0; command argv SHA-256
  1d240fdd5a617183dcbccf09a18ceb43bf5874e9320ebaa322595e06936a0299.

- 2026-10-13T05:19:39+00:00: Recorded command exit 0; command argv SHA-256
  eccde916b32d2eae7dd1e462cee9b4075f16027ce742bffb3d677c8af52ac56b.

- 2026-10-13T05:19:51+00:00: Recorded command exit 0; command argv SHA-256
  963e921db469236b0a745ac7160f3f852a9c83c03c7cf84603a4cdd33be4f503.

- 2026-10-13T05:20:55+00:00: Recorded command exit 0; command argv SHA-256
  d0401fa1b2872e9914e63d54b40a16dd97a8a185c56b36e63a2e291f21836362.

- 2026-10-13T05:21:06+00:00: Recorded command exit 0; command argv SHA-256
  cd09e9b25872d263fc8fa08f8e503e5c81ae0bb1113e48790da33955ec78b6a1.

- 2026-10-13T05:23:16+00:00: Recorded command exit 0; command argv SHA-256
  831c52cf7f5dd2d11483ca003f8e925f44a3ce7781a48af8328f3be81b07bff5.

- 2026-10-13T05:23:37+00:00: Recorded command exit 0; command argv SHA-256
  1f8bb5a902b8a1b83ef70ebfc52346c9cfc098455409a1dede866a444d0c648a.

- 2026-10-13T05:23:50+00:00: Recorded command exit 0; command argv SHA-256
  e33457c5e624e11f6ce286b2661328c28928dd58d111622c9e6d275629c3d076.

- 2026-10-13T05:24:00+00:00: Recorded command exit 0; command argv SHA-256
  d795e79ead8836e242225f8ee7ccfb65d640edff504b5b144526f996a8c558f7.

- 2026-10-13T05:24:09+00:00: Recorded command exit 0; command argv SHA-256
  73c1e7dabe8f1cf3bf3adb5dddbc9629ee9f2f42ff8a6f7187cdae7131974b94.

- 2026-10-13T05:24:17+00:00: Recorded command exit 0; command argv SHA-256
  8e3811c5108345e53cb3cb5c1a5f5031b4399c81a37caa2a406b594461c721c3.

- 2026-10-13T05:24:28+00:00: Recorded command exit 0; command argv SHA-256
  3721c0be40f227a22a98d6d55f48a543fa6e7833a1c8ee59d0d92351214a834e.

- 2026-10-13T05:24:41+00:00: Recorded command exit 0; command argv SHA-256
  11bdbcb7b1557d2144d39ef99908913ec054d3160145423b7697cce2342e8626.

- 2026-10-13T05:24:52+00:00: Recorded command exit 1; command argv SHA-256
  d63a12c8225de2c59304119e0cf234f302d46ca636f18e138903347c16805d8b.

- 2026-10-13T05:25:05+00:00: Recorded command exit 0; command argv SHA-256
  2a735f2f511d785c4b0cba042db05a3b4b91d7463c581995c7f6c3a8a34196ca.

- 2026-10-13T05:25:19+00:00: Recorded command exit 0; command argv SHA-256
  f0a39ba764e97bd740adcfd3f6ee76ba16ba998bff460888d2f1133bda231866.

- 2026-10-13T05:25:39+00:00: Recorded command exit 0; command argv SHA-256
  0c8b4573eb55e8bde995a397fc176290fd47bfc18f067e55154faaa3e336168d.

- 2026-10-13T05:25:55+00:00: Recorded command exit 0; command argv SHA-256
  3eeb3124138b63aa0bc828ec2d908c876c9f7f9c793f30ffca54cea57c4ea169.

- 2026-10-13T05:26:04+00:00: Recorded command exit 0; command argv SHA-256
  0cb935b255e89896e97d377a9d716378ed79c2e5435c31414769b7125ed6ba79.

- 2026-10-13T05:26:22+00:00: Recorded command exit 0; command argv SHA-256
  3723b270cfae9e5b6872639eded7cde8b7a8f29ac3d3a429f281fa0ed3e36e7e.

- 2026-10-13T05:26:34+00:00: PR #304 was merged externally at old head 85e35a62 while independent
  review was withheld for merge-blocking exactly-once and negative-runtime coverage gaps. Published
  follow-up repair PR #305 on merged main c4f554e79c16bcc910b4a9af6a665a230b3339fb: head
  f25720e6c630e80c067182635bca74afc2e96de8, tree c4a37ee8e12d7f8a0d90aa152b7fcfa62436c0b9, binary
  sha256 ef090ca66a2b376324d471686ff68fa5ec375afb62ea5f8573d09afc6357fa20. Exact ASB PR #627
  inherited-fd/PTY qualification passed 1/1 in 4.44s with no exact child leak. Full local gates
  green; independent review assigned and hosted checks pending. Implementation worker did not merge.

- 2026-10-13T05:26:40+00:00: Recorded command exit 8; command argv SHA-256
  f1321eee52d360bb4f66439cc5fc531a2bbb1cf3d330fd1286c14d4719033f4b.

- 2026-10-13T05:31:48+00:00: Recorded command exit 0; command argv SHA-256
  6da14f040e9ee2819ed5a7923a3dc40e7bbcd59d8b1b9918bf275326467e252c.

- 2026-10-13T05:31:59+00:00: Recorded command exit 0; command argv SHA-256
  175abad34884dcee4a3677ebd898b7850809891ff6bb011adf177a251efa3ad8.

- 2026-10-13T05:32:23+00:00: Recorded command exit 0; command argv SHA-256
  89be65a5b4725a9718e170b0f431dfb0b68ffc575d71ade8897b4cc0560a5cf0.

- 2026-10-13T05:32:43+00:00: Recorded command exit 0; command argv SHA-256
  06f13f02f6a4be61cdc359012b05841656b0d68b149c73180616f82a5996ad3b.

- 2026-10-13T05:35:30+00:00: Recorded command exit 0; command argv SHA-256
  82baf969ba3a9881e16c399564f5044407af7d1f1eec0dc48d2dee06cab6a098.

- 2026-10-13T05:35:53+00:00: Recorded command exit 0; command argv SHA-256
  e7b0a75bd3af6756bb7a0f93666642e3083f89f5bd8955a906a31a973e8d389d.

- 2026-10-13T05:36:10+00:00: Recorded command exit 0; command argv SHA-256
  2aeb4afdd5c613801fc52c416c85047e7987e25c5c37a6682147cf9b91854bcf.

- 2026-10-13T05:36:20+00:00: Recorded command exit 0; command argv SHA-256
  7d26c7c195f747a5caa401e8a41afc94d432b5ab4082211fe19d0f88bdb3050d.

- 2026-10-13T05:36:42+00:00: Recorded command exit 0; command argv SHA-256
  377f5e8ecb169783f6d199a0fcf6f819fdaf93511446c233bff7a9740ede3d74.
