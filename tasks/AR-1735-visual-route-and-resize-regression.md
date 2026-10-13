---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T05:33:40+00:00",
  "depends_on": [
    "AR-1732",
    "AR-1733",
    "AR-1734"
  ],
  "id": "AR-1735",
  "next_action": "Await independent exact-head review and hosted CI for PR #303; do not merge without approval.",
  "observed_branch": "feature/ar1735-visual-route-resize-regression",
  "observed_dirty": 0,
  "observed_head": "4cb2c3e21fd86de2fbe9c2acefad8d9f9adb88dd",
  "owner": "codex-asb-tui-ar1735-visual-regression-20261013",
  "plan": "../plans/AR-1735-visual-route-and-resize-regression.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1735.json",
    "spec_revision": 1,
    "status": "planned"
  },
  "spec_ref": "specs/AR-1735.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Qualify the visual fidelity contract across every route, terminal size, color capability, and keyboard-only interaction without source/model/help drift.",
  "task_revision": 118,
  "title": "Qualify visual fidelity across routes, resize, and terminal capabilities",
  "updated_at": "2026-10-13T03:13:51+00:00",
  "worktree_key": "asb-tui-ar-1735-visual-route-resize-regression"
}
---

Visual regressions are product regressions: snapshots must prove hierarchy,
selection visibility, step location, footer help, and small-terminal behavior,
not merely that drawing does not panic.

- 2026-10-13T02:33:37+00:00: AR-1732 through AR-1734 are released; visual regression qualification
  is dependency-ready.

- 2026-10-13T02:33:40+00:00: Claimed by codex-asb-tui-ar1735-visual-regression-20261013.

- 2026-10-13T02:34:04+00:00: Recorded command exit 0; command argv SHA-256
  888e6a0a261cf859bbde85a162a1168960ada0fa6e00053ffc37a21145a22d37.

- 2026-10-13T02:34:18+00:00: Recorded command exit 0; command argv SHA-256
  272b6cb10709084b33ced1947aeb5f37195cf23369b85df5f895cfb596ee392b.

- 2026-10-13T02:34:26+00:00: Recorded command exit 0; command argv SHA-256
  f9911a459ed7ff14b3d418580d81f915ffbb7575c713e322edf715f1e65db495.

- 2026-10-13T02:34:37+00:00: Recorded command exit 0; command argv SHA-256
  a4346e5c9bd20ca0b01ba5e7e10c3a7c702a2535d6afc855a9227160f2120b66.

- 2026-10-13T02:34:47+00:00: Recorded command exit 1; command argv SHA-256
  b42613aae5ee5b04041425261f754ada71792bd09360d57fa187ca18912e5351.

- 2026-10-13T02:34:57+00:00: Recorded command exit 0; command argv SHA-256
  5bd0aa1753bff3951ffdd38869a03be79f541a22cfe0404d8ea58a84dbd3f674.

- 2026-10-13T02:35:06+00:00: Recorded command exit 0; command argv SHA-256
  6d875df4ce27c6666d78d4b7fe9a9ad0554175d2f1a96e8c7669d568372e5523.

- 2026-10-13T02:35:21+00:00: Recorded command exit 0; command argv SHA-256
  a8bfeb160e91d47a16f3c120f2276445704f77a7c5c9d8e783b28b09fa404700.

- 2026-10-13T02:35:29+00:00: Recorded command exit 0; command argv SHA-256
  878718d24dde73a028465ee64c7693c0ccaee0537910be41fb013803a98ed2e0.

- 2026-10-13T02:35:38+00:00: Recorded command exit 0; command argv SHA-256
  276a534e18c2ecadf11c4b86a656cb29b59cfa93d538d1efaa2eec9a4e46a522.

- 2026-10-13T02:36:17+00:00: Recorded command exit 0; command argv SHA-256
  85c9086a6a4d571604b48df4c83c7d622e1a8c0010dc8f1f30af719264b2fd6a.

- 2026-10-13T02:36:25+00:00: Recorded command exit 0; command argv SHA-256
  57b124cae5e959ce30630bd749585eeda149b8c9455c21ee07207dc8523bf6be.

- 2026-10-13T02:36:47+00:00: Recorded command exit 0; command argv SHA-256
  3ccddae2005b71ab0b6b5980cda6c065322fb4ce768adf1f784efd01b93bce40.

- 2026-10-13T02:37:02+00:00: Recorded command exit 0; command argv SHA-256
  88517a0366f4aea70e74dd562d8e934e1869e77d550f868964dd0b793e9a494f.

- 2026-10-13T02:37:39+00:00: Recorded command exit 1; command argv SHA-256
  297d337c91aa9a47d9996e4f13b9417c2e78d51d119a916f5604074c96d1c352.

- 2026-10-13T02:37:50+00:00: Recorded command exit 0; command argv SHA-256
  3425af919df22ae5029ed33f8eca3db4830c2ec1d8236ae50541b7a6bdc41e90.

- 2026-10-13T02:37:59+00:00: Recorded command exit 0; command argv SHA-256
  ba2792054f5d47f1fa0f5a0fe80c14a9ead8e484a2d1a6e0f0a7b6a958fb82c6.

- 2026-10-13T02:38:11+00:00: Recorded command exit 0; command argv SHA-256
  5777517a5a78ef6ea80fdca351a0ac5ec18b53e499d83816c83091d3eeae03bd.

- 2026-10-13T02:38:52+00:00: Recorded command exit 1; command argv SHA-256
  fc036d226eec0a795a2cc8ab8aded892d579b64a941db17b1c6716407608429b.

- 2026-10-13T02:39:26+00:00: Recorded command exit 1; command argv SHA-256
  2206d8c745d8dba1b117e8f099c7d08cf260ec6ad1127b3287dadbe7d2142d34.

- 2026-10-13T02:40:46+00:00: Recorded command exit 0; command argv SHA-256
  a21b469f56cc7db8eeeaefd854952a6a5a481bb71e88904054a8e16e9471740d.

- 2026-10-13T02:41:06+00:00: Recorded command exit 101; command argv SHA-256
  ea8926a3d05e9ced83b7b5334f59b0858e82432b81b2273e7bcdf1fcff629cc9.

- 2026-10-13T02:41:20+00:00: Recorded command exit 0; command argv SHA-256
  63de0c05cdf521e4b08e8f683694938aaec2aff2c6e8caf8f159c3ae5eabac5b.

- 2026-10-13T02:41:35+00:00: Recorded command exit 101; command argv SHA-256
  9b52efa2cb197232e00cc3cc97370447434e5994d76b2cc0ba47f0edc024f6f3.

- 2026-10-13T02:41:46+00:00: Recorded command exit 0; command argv SHA-256
  ba7ea98551e206fb0efa91646883bcb699bac85b9da431cb176a54e11960c1a4.

- 2026-10-13T02:41:55+00:00: Recorded command exit 0; command argv SHA-256
  22b7aba909ee8cfe0a0d14c8deb2cc2315c34184e13efa75bce2903dfbe23adb.

- 2026-10-13T02:42:07+00:00: Recorded command exit 0; command argv SHA-256
  0cbdf433e687b219e74e6142b6dc2980b2d85f3e3c48049fb9721f8fd7e3d0f6.

- 2026-10-13T02:42:16+00:00: Recorded command exit 0; command argv SHA-256
  d5313f6a8c556e84dc415224d5e72d2376d7d8686829faf41d155e8ad979690e.

- 2026-10-13T02:42:27+00:00: Recorded command exit 0; command argv SHA-256
  3fa2bd2243787f66b29958426265311b99e66bcc7b1ce8e0f4dbeaa68528bc2a.

- 2026-10-13T02:42:47+00:00: Recorded command exit 1; command argv SHA-256
  a60b8b1e7e976c59ea94b933a9c9f73f32ed141f4a828c8eb7005f057c2f9d3b.

- 2026-10-13T02:43:05+00:00: Recorded command exit 0; command argv SHA-256
  392c7eda2a51815acb62029d5a39644228ec3e9433d7b5e1f402144dc1fe75ab.

- 2026-10-13T02:43:26+00:00: Recorded command exit 0; command argv SHA-256
  0fb56703ae14730f2b579af3856c22df1c186cfb46c220101eed9341ccd6c509.

- 2026-10-13T02:43:34+00:00: Recorded command exit 1; command argv SHA-256
  32766024a2d7169c996a3f2e70421a985faa1b0d673317a104c2be3317c44dd6.

- 2026-10-13T02:43:49+00:00: Recorded command exit 101; command argv SHA-256
  7dbe692d6ec10ead3c50d2cca9de2b18481a92820ffa3ee812f7aaeeb42ca455.

- 2026-10-13T02:44:04+00:00: Recorded command exit 0; command argv SHA-256
  79ea9b50f0b5e116fd28274d637257a1687bcf447588d9891fdd4d94d20d1560.

- 2026-10-13T02:44:14+00:00: Recorded command exit 101; command argv SHA-256
  fd70f9aacaf1afb75b9ecff0a19a913451f3f4ae0bc7cdf8fdacf1be8f0ff3c1.

- 2026-10-13T02:44:27+00:00: Recorded command exit 101; command argv SHA-256
  5938c70daabcf38e6970f2d5b653a8444d68b2bc750490ec62cb807917ddf823.

- 2026-10-13T02:44:44+00:00: Recorded command exit 0; command argv SHA-256
  ae69d5ff48e41ace044de034b7e304a4077267510b8a1bb6d50cc67b93835c33.

- 2026-10-13T02:44:56+00:00: Recorded command exit 1; command argv SHA-256
  4a51ac20cad1fd0f1b04e2ecab0eaeda63fa432fe9bbe0294ecc092508ea6a60.

- 2026-10-13T02:45:03+00:00: Recorded command exit 0; command argv SHA-256
  93cab40ce3cbfa911ffea1a162c839dbf223059a60ce101bfe37f6a314b0e997.

- 2026-10-13T02:45:14+00:00: Recorded command exit 1; command argv SHA-256
  5de893e31071e7039d95b572088dc241db86fa59cf938007a65e2799c5db28a9.

- 2026-10-13T02:45:21+00:00: Recorded command exit 0; command argv SHA-256
  f775c0df1e3be9f34f7302d54e129fc9865a96b5f20b1b9baf967a1eb3dbde23.

- 2026-10-13T02:45:35+00:00: Recorded command exit 0; command argv SHA-256
  1c7b9f7fab87addb1f2ebef1c8eaf4f54ae77093ab3003f3edf8c7a99389ae8d.

- 2026-10-13T02:45:51+00:00: Recorded command exit 0; command argv SHA-256
  17e09c68b5753370ce850b163c303020756ea5604e19f08ba6f40f49edfeedce.

- 2026-10-13T02:46:10+00:00: Recorded command exit 0; command argv SHA-256
  380d20b058caae1f8bd04c882ea6caa186771233251d88dd66a710a7ee703af6.

- 2026-10-13T02:46:59+00:00: Recorded command exit 0; command argv SHA-256
  d7bdd5e877cde102ffca6da02ba78352df050db3573346f225a777f6c1a203a4.

- 2026-10-13T02:47:27+00:00: Recorded command exit 101; command argv SHA-256
  f6ac53f5ea203b834adb002ca3fa3be351ff125d7be7a1bcde493ff2a859b36d.

- 2026-10-13T02:47:47+00:00: Recorded command exit 101; command argv SHA-256
  9e9cb3f4aff34dc464eb311af19b436394d00a0ab68021327f3cae8cbf2d94b8.

- 2026-10-13T02:48:00+00:00: Recorded command exit 0; command argv SHA-256
  2f1304fd0cda09bac2e53b2c43dc4c0c454b9f16f17f92cd04ded0c4c8c03887.

- 2026-10-13T02:48:11+00:00: Recorded command exit 0; command argv SHA-256
  a0183af9224949d6d430c5941c9f5cd8b64c50735ed536c189896d7b47a53e00.

- 2026-10-13T02:48:21+00:00: Recorded command exit 0; command argv SHA-256
  e13025828c9885a620dd686bf463bb9ce39918311658bf5d8ed1b9199e07b8cf.

- 2026-10-13T02:48:42+00:00: Recorded command exit 0; command argv SHA-256
  255cc64829979937bdca9c3c168b106878d49f8e8cc2ac63be2eccc96f0fb0d0.

- 2026-10-13T02:49:02+00:00: Recorded command exit 101; command argv SHA-256
  005db6fd062136d4b35be9e68ebbdbb6f4ee429d8d721183529ef4ed296a10f6.

- 2026-10-13T02:49:20+00:00: Recorded command exit 101; command argv SHA-256
  3ae631a7784786ea4a4fab7aad3410e7927f9e47868d20a3ebb043a3340aa203.

- 2026-10-13T02:49:34+00:00: Recorded command exit 0; command argv SHA-256
  10c3592497ae53884838e864ad88c9a38a5a5c4c83af11fd9ae3206866d02c2e.

- 2026-10-13T02:51:38+00:00: Recorded command exit 0; command argv SHA-256
  661d06af91a57bd50080aeba33495bd53ed88260a1bb15fdb3780bd741cb4d9f.

- 2026-10-13T02:52:49+00:00: Recorded command exit 1; command argv SHA-256
  d6cfb6a588afd75e24e2b695778e614c82e720a02541c9ea6385bc196506812d.

- 2026-10-13T02:52:59+00:00: Recorded command exit 0; command argv SHA-256
  a1d1593526d7d2b88265d71e4f1f9f0b0189cb9f434d9f8fe9015d2d34f30b2d.

- 2026-10-13T02:53:30+00:00: Recorded command exit 0; command argv SHA-256
  cef4d06e82c0ae704279e419accc26192bdf8823b29263897c5d1ad4ab45a7af.

- 2026-10-13T02:53:58+00:00: Recorded command exit 0; command argv SHA-256
  98065b48a598372d0c5f994168e73706b4b083fc1be7677707a46338045bc6e5.

- 2026-10-13T02:54:10+00:00: Recorded command exit 0; command argv SHA-256
  70989e84a147179dd3fff7f8258ef2fdd5c41c22f6609c0abeabf1724bc32825.

- 2026-10-13T02:54:18+00:00: Recorded command exit 0; command argv SHA-256
  2d9baa6d673f14a034acf2f7b89233b04de597806a97666e4d1659c0ba0cde7d.

- 2026-10-13T02:54:29+00:00: Recorded command exit 0; command argv SHA-256
  be0d3daf186d583505aee98a3466a15bd68084d390a8c43dd87c3b0954a640df.

- 2026-10-13T02:55:26+00:00: Recorded command exit 0; command argv SHA-256
  ff2e5234b841b2efa403041f5854ec25639d5b544611c905ded0cb909e5e0057.

- 2026-10-13T02:55:39+00:00: Recorded command exit 0; command argv SHA-256
  68e0cf9e84c38931f383038f1ef4bf3ea38be54bfe414265280995d09690824a.

- 2026-10-13T02:55:52+00:00: Recorded command exit 0; command argv SHA-256
  bc84e39754ad7b84bb2ba8c4c8a09b66d5fc8d7de0e9968805b29131d8dddac9.

- 2026-10-13T02:55:59+00:00: Recorded command exit 0; command argv SHA-256
  5d3b5f4be1641dd2fd0732c7af4d3b7632204c61c323bd3a74387ef89855f787.

- 2026-10-13T02:56:08+00:00: Recorded command exit 0; command argv SHA-256
  cb77f983a968bcf460b2f320f4e889db68b11bef668cc9b3cf3080faaa2a99c1.

- 2026-10-13T02:56:19+00:00: Recorded command exit 0; command argv SHA-256
  88517a0366f4aea70e74dd562d8e934e1869e77d550f868964dd0b793e9a494f.

- 2026-10-13T02:56:31+00:00: Recorded command exit 0; command argv SHA-256
  fc634293c65d47111ef59ca7ab880a4af551c76510beeb13753d4a3c6c065655.

- 2026-10-13T02:58:10+00:00: Recorded command exit 1; command argv SHA-256
  234ec25a0104d7cdd8c01f9f5d922a3a0a8f5681c623ab915af58246f4bf0fb6.

- 2026-10-13T02:58:30+00:00: Recorded command exit 0; command argv SHA-256
  57c4f3675351a9b79c4f300a626f2807e7f9866e4561cb08fe1067b5b2f77367.

- 2026-10-13T02:58:58+00:00: Recorded command exit 0; command argv SHA-256
  2055f3480d7a0c8d9ae88dc1eaf01b832a8cd30c6d6330cc7a1b1c5588666b02.

- 2026-10-13T03:00:50+00:00: Recorded command exit 0; command argv SHA-256
  073cc038cdbe36146f84c4365097a5e48bce53d05ed3f98956fc3f817a09551a.

- 2026-10-13T03:01:03+00:00: Recorded command exit 2; command argv SHA-256
  f6328d8d583a58d5d647e0c6a5bb6f33564ccd269b1ff948069355dd7788022e.

- 2026-10-13T03:01:11+00:00: Recorded command exit 0; command argv SHA-256
  fb50fcf2a6dce300f36c8050c8420614974e313bc9c33adeff1a779d32fa79b3.

- 2026-10-13T03:01:19+00:00: Recorded command exit 0; command argv SHA-256
  fd37ea25428b5f20414881bffc65191352da76fc448eee54686bced7b0762f31.

- 2026-10-13T03:01:29+00:00: Recorded command exit 0; command argv SHA-256
  893711c427c46884e28db9481737213a497abfac275d19c505d260e173216d69.

- 2026-10-13T03:01:39+00:00: Recorded command exit 1; command argv SHA-256
  125ef030fbcf3e3ee69b05a8e5083356ba4c9030b7f963c5c1703f75b14bc03f.

- 2026-10-13T03:01:48+00:00: Recorded command exit 0; command argv SHA-256
  94ba17cbf9f9fb40b0c06fb7a1816cfc9748de29bcd9a6c4f51599f8e9bd36d9.

- 2026-10-13T03:01:58+00:00: Recorded command exit 0; command argv SHA-256
  dd2762641f42fc1f1f497d6cb6756e801469b2d716fa2673429d425ef7d1dab9.

- 2026-10-13T03:02:09+00:00: Recorded command exit 0; command argv SHA-256
  743a8486d6e1724ed9e3942382a602ec2a15046bc01ff8d06e017132726a4cca.

- 2026-10-13T03:03:25+00:00: Recorded command exit 0; command argv SHA-256
  915e3765324c7c4d3386b5b619849eb64cd5a3425a58c04640816e918fc8dfd9.

- 2026-10-13T03:03:47+00:00: Recorded command exit 101; command argv SHA-256
  b6603defd5c16151584c59e7c123fc241a2b7033d4e7bcb8979f39e34af1c42a.

- 2026-10-13T03:05:46+00:00: Recorded command exit 0; command argv SHA-256
  689f6b1f60bcec1f096181c99af73b4b73bf7746ddf2b5ada4d2d94ace02183c.

- 2026-10-13T03:05:58+00:00: Recorded command exit 0; command argv SHA-256
  c7b3cfd4b3eac2a66ae49379fe630d307bb83974477840bf595e9066ce50251d.

- 2026-10-13T03:06:08+00:00: Recorded command exit 0; command argv SHA-256
  650af25317b51cc11808fe675bccc6d3644c7a0cc73e77ff35ad7f3bc91f19a2.

- 2026-10-13T03:06:23+00:00: Recorded command exit 0; command argv SHA-256
  99e047aeb00fae9ddcf0295b9d9392d024b8f0641a556ed2c793dd021801fb32.

- 2026-10-13T03:06:40+00:00: Implementation candidate published as PR #303. Exact base
  3d978ba716f17ed9c11ca7f732c646e68a06ab7f, signed+DCO head
  4cb2c3e21fd86de2fbe9c2acefad8d9f9adb88dd, tree 9e3c4634a82439f51a08539c629ab94e93f047e5. Full
  cargo test, clippy, fmt, rustdoc, release build, coverage (90.29% lines),
  visual/formal/source/help/tutorial/journey/publication/release/shell/workflow/Gitleaks gates
  passed. Terminal foundation 33/33 and full/coverage runs proved zero surviving exact ASB TUI
  children. Local cargo-deny/cargo-audit commands unavailable; hosted gates remain required.

- 2026-10-13T03:06:47+00:00: Recorded command exit 0; command argv SHA-256
  18a2be3a706744a56fec350e8d671be94e9451dee4f55da072ae1938c11701ab.

- 2026-10-13T03:07:05+00:00: Recorded command exit 0; command argv SHA-256
  ac9cbf9a7da301f4e29cf27b6a4bf93ca32dde3d2f60724d4c5431f19153d9cc.

- 2026-10-13T03:08:30+00:00: Recorded command exit 0; command argv SHA-256
  ac9cbf9a7da301f4e29cf27b6a4bf93ca32dde3d2f60724d4c5431f19153d9cc.

- 2026-10-13T03:09:46+00:00: Recorded command exit 0; command argv SHA-256
  010151394b9833008a4229589de9bf04a6052e000153130b8223c53e866f46aa.

- 2026-10-13T03:10:53+00:00: Recorded command exit 0; command argv SHA-256
  c5eda45556cd45d0edf7282bd5a2031a4f4c27468ce31583796fc894a224fce9.

- 2026-10-13T03:11:05+00:00: Recorded command exit 0; command argv SHA-256
  afbef7cfca11bf72792b1f20a2ad1900c0887a605db3f6b428b087adf07ee186.

- 2026-10-13T03:11:50+00:00: Recorded command exit 0; command argv SHA-256
  442ab4d1b1866855bc93c44cd922833dda555da5780684b4813508b5b679f57d.

- 2026-10-13T03:11:59+00:00: Recorded command exit 0; command argv SHA-256
  afe4c459578225fdf9efe26b608acb6383a0ea1066d916345806a6718dc773f1.

- 2026-10-13T03:12:11+00:00: Recorded command exit 0; command argv SHA-256
  90f1b2ee22dc0d6f1455290246c5ab6b6d8caf816a635cb7454ac9ffb9675bfe.

- 2026-10-13T03:12:20+00:00: Recorded command exit 0; command argv SHA-256
  30d7283f56001ed57abf12a2371c8483b05330841d2e7f69dad7a92ab988cfeb.

- 2026-10-13T03:12:58+00:00: Recorded command exit 0; command argv SHA-256
  76337ff6f3809ff02821bd6adf13cb8c0e7d173f9b8376d9050abc416e667cf4.

- 2026-10-13T03:13:10+00:00: Recorded command exit 0; command argv SHA-256
  6194808c8ccedd9f065a05a823e50174b32df7eeda696067a99c55cfca7c51d9.

- 2026-10-13T03:13:18+00:00: Recorded command exit 0; command argv SHA-256
  527b8d62ceee19e4a3df76594e21234910397f76a60a73332019fee741988c1d.

- 2026-10-13T03:13:37+00:00: Recorded command exit 0; command argv SHA-256
  75096640cdbff2df57150269ac112abdce057c67c6a243ca46b152e5c51257ba.

- 2026-10-13T03:13:51+00:00: Recorded command exit 0; command argv SHA-256
  6d2be97ea8e3c08d546d7575177e2fa22ee162946f023fd9ef2d6698e8fa44ff.
