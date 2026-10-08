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
  "next_action": "Parent coordinator may merge independently reviewed PR 292; after merge, verify exact origin/main post-merge gates and requalify AR-1597. This worker must not self-merge.",
  "owner": "codex-ar1723-low-typing-20261008",
  "plan": "../plans/AR-1723-low-typing-wizard-controls.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the supported fresh-user wizard path use bounded selections and safe defaults instead of free-form configuration, credential-reference, recording-mode, and replay-policy entry.",
  "task_revision": 98,
  "title": "Replace wizard free-form setup with bounded controls",
  "updated_at": "2026-10-08T08:22:53+00:00",
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

- 2026-10-08T07:50:17+00:00: Recorded command exit 0; command argv SHA-256
  8066745c0e1254e25dfee4586ad7e603da6aa2fa5759a72fa0e4c7180b91adcc.

- 2026-10-08T07:50:29+00:00: Recorded command exit 0; command argv SHA-256
  e0c82a84e85a2c7dc1ea64520cd0f1fa5dc00e32744c1b4b0181387ed539206f.

- 2026-10-08T07:50:40+00:00: Recorded command exit 0; command argv SHA-256
  08ec1e826a1723fe86ef76dcf83b3782496b4ab997fb80fa6126e19530b744d1.

- 2026-10-08T07:50:52+00:00: Recorded command exit 0; command argv SHA-256
  ab6f31dd8c7618b8854daf6e17ee2acbf498f9bb813d5a8a15a52a7ddfcd7eea.

- 2026-10-08T07:51:24+00:00: Recorded command exit 0; command argv SHA-256
  22652158b656ead6aaee2f7d7f9c9602c3302c37b733b355be38a03406e9dc43.

- 2026-10-08T07:51:44+00:00: Recorded command exit 0; command argv SHA-256
  5fb1bbfa38dd2665bf9c9a77e76000463affc0912566f90301bc990541806440.

- 2026-10-08T07:52:08+00:00: Recorded command exit 101; command argv SHA-256
  777b980ec6d937f40c1cb1cec62510e0e7f37e67f0bc9f1ff29c89d11fdd028e.

- 2026-10-08T07:52:54+00:00: Recorded command exit 0; command argv SHA-256
  a71d7cf2d673427d253074b45190b28836b2647a35d33d051fed592b02cb3ddd.

- 2026-10-08T07:53:12+00:00: Recorded command exit 0; command argv SHA-256
  e6b923377d5b9b70568a1248b31388b22bd0361a2a8dc43f7f38e206dc3b1e8b.

- 2026-10-08T07:53:28+00:00: Recorded command exit 0; command argv SHA-256
  56ea78546557b4d20fb3fa464ad2abf897e112eb166b0e68368531e9097f1eb5.

- 2026-10-08T07:53:43+00:00: Recorded command exit 0; command argv SHA-256
  54799b026d4f3be4fd9def27da79ac0412f0cae174efa50ee9e54fc23da8def3.

- 2026-10-08T07:53:56+00:00: Recorded command exit 0; command argv SHA-256
  2b7b832dc3a49e845eee4c3d8d7fe5471ffd948e2854cca2ee694afb54f653d0.

- 2026-10-08T07:54:16+00:00: Recorded command exit 0; command argv SHA-256
  5fb1bbfa38dd2665bf9c9a77e76000463affc0912566f90301bc990541806440.

- 2026-10-08T07:55:18+00:00: Recorded command exit 101; command argv SHA-256
  777b980ec6d937f40c1cb1cec62510e0e7f37e67f0bc9f1ff29c89d11fdd028e.

- 2026-10-08T07:56:28+00:00: Recorded command exit 0; command argv SHA-256
  dfa2868d93e40309f5ac49421732d4463c54a863f174ca497530b09f8bf7197b.

- 2026-10-08T07:58:20+00:00: Recorded command exit 101; command argv SHA-256
  e2a1fd1d22aa6440a4789d156d676cf60cecb32ee7cd00cce20635d694caee1b.

- 2026-10-08T07:58:40+00:00: Recorded command exit 0; command argv SHA-256
  a71d7cf2d673427d253074b45190b28836b2647a35d33d051fed592b02cb3ddd.

- 2026-10-08T07:58:55+00:00: Recorded command exit 0; command argv SHA-256
  edf0f8e473a0598b88f1d4139864b51f7675d16337aa57805ac574621d63eac4.

- 2026-10-08T07:59:10+00:00: Recorded command exit 0; command argv SHA-256
  24be19ea945c12f0572568dd734b8bc5ef300c788e06b19a21cc20399196f340.

- 2026-10-08T08:00:58+00:00: Recorded command exit 0; command argv SHA-256
  6fa010fac95af1940058b73a92591491b22a4dbe7d8999cca19645b140ec1e73.

- 2026-10-08T08:01:23+00:00: Recorded command exit 0; command argv SHA-256
  5da14168bf02d9655493d98e327f54d03a9e6e6030623f24049c35d67f2de248.

- 2026-10-08T08:01:36+00:00: Recorded command exit 0; command argv SHA-256
  362702b3ce62baf2a0a9d91f0a7e43c889654ab289efd22acdd46e530303e759.

- 2026-10-08T08:01:47+00:00: Recorded command exit 0; command argv SHA-256
  1b8de66859532f19d3ac49e88ff3284df7c10d57bbd4c1f3d267a921f57d43db.

- 2026-10-08T08:02:00+00:00: Recorded command exit 0; command argv SHA-256
  5990bb51b546d9d8f57a3230063652dbc817ce0286de34446ced26af340e6c3b.

- 2026-10-08T08:02:14+00:00: Recorded command exit 0; command argv SHA-256
  bea143c4f046bfb5064d0425e65517434a89d2ceea114456415464e555a1b730.

- 2026-10-08T08:02:26+00:00: Recorded command exit 0; command argv SHA-256
  b885c82a72cb23e26f684d9d12348909158471cca2dfa6a2b7036a1e17788bd7.

- 2026-10-08T08:02:39+00:00: Recorded command exit 0; command argv SHA-256
  d69673eef1287cd9f03d4f3d2d6ab2f0f5705b9260990bc7975189eb7935bddb.

- 2026-10-08T08:02:50+00:00: Recorded command exit 0; command argv SHA-256
  5a3adb5ab1a92b790be7f0af219f16bf672685cdaf7b2cdabb61282f128699f2.

- 2026-10-08T08:03:09+00:00: Recorded command exit 0; command argv SHA-256
  5d05856a0f761f64012727e0bcf24a9d36dc203e22034427990864273cbf385f.

- 2026-10-08T08:03:22+00:00: Recorded command exit 0; command argv SHA-256
  597c4404df6d9dfbbf61ff89ad5da7c819e1682d0af13c959880ab2f0a292042.

- 2026-10-08T08:03:40+00:00: Recorded command exit 0; command argv SHA-256
  d5c0371f3b6d07f7cb8c30b0dbd4fd28f1e3593026d6b6fec852204630527906.

- 2026-10-08T08:04:32+00:00: Recorded command exit 0; command argv SHA-256
  f022179fc1b4a704a30915c650c678f681410bbca3d68c02034b1bd9d5322227.

- 2026-10-08T08:04:58+00:00: Recorded command exit 0; command argv SHA-256
  08f988e8492b215c6c4ef0e4a7bce306398a146523d987f3c67f336e636a6590.

- 2026-10-08T08:05:11+00:00: Recorded command exit 0; command argv SHA-256
  d76108b017910b96f00e6fb27008120d5c5be20e7057f6f2c6de41d2769361f0.

- 2026-10-08T08:05:24+00:00: Recorded command exit 0; command argv SHA-256
  11893d1057db8c9656808695863373c6e2f8dd410610c27807259220532226bb.

- 2026-10-08T08:05:37+00:00: Recorded command exit 0; command argv SHA-256
  7141e950a948cbda8d758541c66523c23a8186d4d0128cdd5fc23bf890f60746.

- 2026-10-08T08:06:02+00:00: Recorded command exit 0; command argv SHA-256
  2cd43204cc843c5d0a5ddb6606acd5fe3097c659bd9fe4c64439165b0346e2b7.

- 2026-10-08T08:06:16+00:00: Recorded command exit 0; command argv SHA-256
  0e189bef278cf65beeb5d1bfb902eec114dbdaebcf02f742c6a9757df655cf59.

- 2026-10-08T08:06:30+00:00: Recorded command exit 1; command argv SHA-256
  eb39c05adc20706dc961f6d73274e3b2e116080dd352b4d02aaf56bd14e39ef3.

- 2026-10-08T08:07:06+00:00: Recorded command exit 0; command argv SHA-256
  4a7d6fbbf7a270a5c472d75f8011b694518f88d8b8bf817e9d3120a038fc95cc.

- 2026-10-08T08:07:23+00:00: Recorded command exit 0; command argv SHA-256
  e8ccf5ef27b64dd21e06361d45f87f27a0ea811f2b126cc8951b69b271ef5099.

- 2026-10-08T08:07:37+00:00: Recorded command exit 0; command argv SHA-256
  ac3faf706b289f1ad357b241f63b4ceeec28fcefae13cb317fea7751f0f4f5d6.

- 2026-10-08T08:07:48+00:00: Recorded command exit 0; command argv SHA-256
  d23ab5b66a75e7a19903d695bebab773b39fae588d187c879c9f0ad8cbbde602.

- 2026-10-08T08:08:00+00:00: Recorded command exit 0; command argv SHA-256
  161a9b9b68682059224e50c9d2d9c223f8967df73c1cafd795d951f8b9a24eba.

- 2026-10-08T08:08:17+00:00: Recorded command exit 0; command argv SHA-256
  d578e905ef5676aff7c6b556c8624abd09f97c4731033526b68577222920ab92.

- 2026-10-08T08:09:18+00:00: Recorded command exit 0; command argv SHA-256
  22652158b656ead6aaee2f7d7f9c9602c3302c37b733b355be38a03406e9dc43.

- 2026-10-08T08:09:33+00:00: Recorded command exit 0; command argv SHA-256
  1226875922e6b327153f8dc86f6911916d180cb1fe1df291c982cb7a319ec4b5.

- 2026-10-08T08:09:45+00:00: Recorded command exit 0; command argv SHA-256
  32306c075293bfdb15c2c3df740a2df1d35d8aa5c717baedb0433d91481f21c2.

- 2026-10-08T08:10:01+00:00: Recorded command exit 0; command argv SHA-256
  5fb1bbfa38dd2665bf9c9a77e76000463affc0912566f90301bc990541806440.

- 2026-10-08T08:11:58+00:00: Recorded command exit 0; command argv SHA-256
  6fa010fac95af1940058b73a92591491b22a4dbe7d8999cca19645b140ec1e73.

- 2026-10-08T08:12:19+00:00: Recorded command exit 0; command argv SHA-256
  e8ccf5ef27b64dd21e06361d45f87f27a0ea811f2b126cc8951b69b271ef5099.

- 2026-10-08T08:12:32+00:00: Recorded command exit 0; command argv SHA-256
  6e6cc052db352cb653fc7fa1b76bdb94b8a8ae7cea93dfffa9d7a984aa039b3c.

- 2026-10-08T08:12:43+00:00: Recorded command exit 0; command argv SHA-256
  d05245e477cfd1eeb29c158823e2437333e999ff1a56c7edd1b3910a4407a6b3.

- 2026-10-08T08:13:01+00:00: Recorded command exit 0; command argv SHA-256
  ac3faf706b289f1ad357b241f63b4ceeec28fcefae13cb317fea7751f0f4f5d6.

- 2026-10-08T08:13:14+00:00: Recorded command exit 0; command argv SHA-256
  ac9bb202049fbb939791de7cc699c5541209c49ea7d5a5a5de37fa3ea6ef133b.

- 2026-10-08T08:13:26+00:00: Recorded command exit 0; command argv SHA-256
  7b66ca64ecee4e090778208d157eda0a0deb9adb047b704c9beed31d752b69c0.

- 2026-10-08T08:13:39+00:00: Recorded command exit 0; command argv SHA-256
  a6e307fa596408a4416d59fc536daf11816f3bf847f437c996a0842d7ea64d59.

- 2026-10-08T08:13:58+00:00: Recorded command exit 0; command argv SHA-256
  bcb9c811648c4ef334d03ca97a072d2abee86cbdab1e9c9e22ac29a0397f18d6.

- 2026-10-08T08:14:20+00:00: Recorded command exit 0; command argv SHA-256
  3d17a1a28e1c455d1791fbd3604990afc2336529fbdc501d0b90f098496072ad.

- 2026-10-08T08:14:47+00:00: Published signed+DCO candidate PR 292. Exact head
  0b2012d1252a4e97c586a029e25ad0f003db3d99, tree d91bca589bf8dca0fbb52a83a5572d3969c515e7.
  Authoritative renderer route reports selection=3, navigation=1, confirmation=6, free-form=0,
  total=10. Full locked Rust suite and repository quality gates passed locally, including
  formal/help/UI_OWNERS/source parity, privacy, restart, cancellation, journey, documentation,
  promoted self-test, and product shell quality.

- 2026-10-08T08:15:09+00:00: Recorded command exit 8; command argv SHA-256
  db6ac697b54def18a536322794319e60a75a8d6a2ec2dcbfb3ae8b57a9cca566.

- 2026-10-08T08:15:59+00:00: Recorded command exit 8; command argv SHA-256
  db6ac697b54def18a536322794319e60a75a8d6a2ec2dcbfb3ae8b57a9cca566.

- 2026-10-08T08:16:50+00:00: Recorded command exit 0; command argv SHA-256
  c5def8ab54a369b2da86df080c198ff23f9328e7fbe0794f57247d1e3ae936b7.

- 2026-10-08T08:17:35+00:00: Recorded command exit 8; command argv SHA-256
  db6ac697b54def18a536322794319e60a75a8d6a2ec2dcbfb3ae8b57a9cca566.

- 2026-10-08T08:17:52+00:00: Recorded command exit 0; command argv SHA-256
  54204c1513815dea5004074d06a63f861092e5bccc43ec72e8b2f4738fc20eb0.

- 2026-10-08T08:18:22+00:00: Independent exact-head review APPROVED with no P0/P1/P2 findings at
  head 0b2012d1252a4e97c586a029e25ad0f003db3d99 tree d91bca589bf8dca0fbb52a83a5572d3969c515e7.
  Reviewer independently verified signed+DCO provenance, 10 counted keys with zero free-form input,
  bounded controls, privacy, fail-closed modes, formal/help/UI owner parity,
  restart/cancellation/stale fences, and focused journeys. PR remains unmerged while hosted checks
  run.

- 2026-10-08T08:19:05+00:00: Recorded command exit 8; command argv SHA-256
  db6ac697b54def18a536322794319e60a75a8d6a2ec2dcbfb3ae8b57a9cca566.

- 2026-10-08T08:19:21+00:00: Recorded command exit 0; command argv SHA-256
  54204c1513815dea5004074d06a63f861092e5bccc43ec72e8b2f4738fc20eb0.

- 2026-10-08T08:20:12+00:00: Recorded command exit 8; command argv SHA-256
  db6ac697b54def18a536322794319e60a75a8d6a2ec2dcbfb3ae8b57a9cca566.

- 2026-10-08T08:21:32+00:00: Recorded command exit 0; command argv SHA-256
  c8fe0760c47502a083319613b0d941a70608c57e9a528e5a264c6eaf453a1d97.

- 2026-10-08T08:21:45+00:00: Recorded command exit 0; command argv SHA-256
  a0db5c724a5b224a08e51e27d497c1248942dc0bee0afe1daffe8a1938aa4b3b.

- 2026-10-08T08:22:02+00:00: Recorded command exit 0; command argv SHA-256
  db6ac697b54def18a536322794319e60a75a8d6a2ec2dcbfb3ae8b57a9cca566.

- 2026-10-08T08:22:15+00:00: Recorded command exit 0; command argv SHA-256
  e362cc1d79ac2aca07e6839804a90eba7352ff2db48a5581b0ff82d8d0045abb.

- 2026-10-08T08:22:28+00:00: All hosted PR 292 checks passed at exact head
  0b2012d1252a4e97c586a029e25ad0f003db3d99: native Rust/supply-chain/privacy gate 6m13s, required
  native-first gate 6m20s, and AWQ v0.32.0 observation 21s. Independent review already approved with
  no findings. Candidate is merge-ready but remains unmerged by this worker.

- 2026-10-08T08:22:31+00:00: Recorded command exit 0; command argv SHA-256
  61a449187ba93f94cb152db730b4bf3a7665db149cbf105fe8af34e0f564727b.

- 2026-10-08T08:22:43+00:00: Recorded command exit 0; command argv SHA-256
  af8e201b59a5220c03ab55b96a084dcefe7542dc894471f0584f92e3fed4dbea.

- 2026-10-08T08:22:53+00:00: Recorded command exit 0; command argv SHA-256
  e890aca3a8d0c3b9960ac37118f67e6b5a1be9545bee380855c91203bb6a706b.
