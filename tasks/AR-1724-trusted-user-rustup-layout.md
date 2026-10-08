---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T12:37:58+00:00",
  "depends_on": [
    "AR-1714",
    "AR-1723"
  ],
  "id": "AR-1724",
  "next_action": "Await independent review and hosted checks for PR #293 at exact signed head 2f8c9a821e1b23e20a23562f524eba2e0c698e54; author must not self-merge.",
  "owner": "codex-ar1724-rustup-layout-20261008",
  "plan": "../plans/AR-1724-trusted-user-rustup-layout.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Accept the conventional owner-owned group-writable Rustup development layout with an explicit warning while keeping executable and substitution boundaries fail-closed.",
  "task_revision": 60,
  "title": "Trusted owner Rustup layout and detached quickstart repair",
  "updated_at": "2026-10-08T09:03:42+00:00",
  "worktree_key": ""
}
---

AR-1597 exact-main requalification showed that the standalone TUI returns
`development_tool_unavailable` for the current host conventional Rustup shim:
the shim and resolved toolchain executables are regular, owner-controlled and
non-writable by group/other, while owner-controlled Rustup directories and
`settings.toml` use the common group-writable development layout. Current ASB
already accepts this narrow layout with a visible development warning.

Repair only the standalone `asb-tui` implementation and qualification tools.
Development authentication, signatures, and key management remain visible
warnings and never block local/mock execution. Do not modify ASB product code.


- 2026-10-08T08:37:55+00:00: Dependencies AR-1714 and AR-1723 are done. AR-1597 exact-main
  reproduction proves the conventional owner-owned Rustup layout and detached-wrapper gaps;
  implement the narrow TUI-only repair with hostile-path rejection.

- 2026-10-08T08:37:58+00:00: Claimed by codex-ar1724-rustup-layout-20261008.

- 2026-10-08T08:38:14+00:00: Recorded command exit 0; command argv SHA-256
  ebb630ca5026e9d1b388242e978e236f440f70b35548843e8a081a9f7f738a81.

- 2026-10-08T08:38:32+00:00: Recorded command exit 0; command argv SHA-256
  fa38fddc44bfcc1230a8ebafa4fdd340651525b4b50c3e6e15e2d8541b1ffa81.

- 2026-10-08T08:38:52+00:00: Recorded command exit 0; command argv SHA-256
  b5e8c5b81a87760c70c2b7a855f6b119e2fe76e5b964c0c87d2d0907788278fb.

- 2026-10-08T08:39:10+00:00: Recorded command exit 0; command argv SHA-256
  a1d18de80fa5f703b1d0f88ead586ab6f97630e1a8ab58551d2697cf9dbb1c0c.

- 2026-10-08T08:39:29+00:00: Recorded command exit 0; command argv SHA-256
  86a182dbe7edd09136403ebe8b230e7332decb669891fee5a788ce9f0a8ac1a0.

- 2026-10-08T08:39:53+00:00: Recorded command exit 0; command argv SHA-256
  7461789e9f5d1b6824bc7cdcc4ff4e00749879e258475d5d6cb941b183ab6bec.

- 2026-10-08T08:40:20+00:00: Recorded command exit 0; command argv SHA-256
  e2ec55bcdea0e985546f5e32b7d2b24f65de417704cd5d1575e8d2c5398a6ff2.

- 2026-10-08T08:40:40+00:00: Recorded command exit 0; command argv SHA-256
  bfe30f89e0542c5243af2c577106ddfe00ae2a5ed6ced11b41cd24ffea6cbde2.

- 2026-10-08T08:42:23+00:00: Recorded command exit 101; command argv SHA-256
  63966ca07ebaf85f77014d0f83c2ab4e3037f079c7fe5f3b8373877450d415cb.

- 2026-10-08T08:42:50+00:00: Recorded command exit 0; command argv SHA-256
  29a6a451f7e6928b3dbff1bd393cd198484cf7a19e56a3db75f26b725f0b2eaa.

- 2026-10-08T08:43:52+00:00: Recorded command exit 0; command argv SHA-256
  38e4690de1f70789fdae5a0b65a0bad1118548f5f015f2369cda9f5eefc74c9a.

- 2026-10-08T08:44:17+00:00: Recorded command exit 101; command argv SHA-256
  59197a9b96e3cf5c5e5efb4efcfd9e5d609c3bd0a12ca7d7696905c854830cc4.

- 2026-10-08T08:44:42+00:00: Recorded command exit 0; command argv SHA-256
  0cf1d5a99643768ac695a477b5e55deb1fe50d910051006797baeee962127bd0.

- 2026-10-08T08:45:14+00:00: Recorded command exit 101; command argv SHA-256
  59197a9b96e3cf5c5e5efb4efcfd9e5d609c3bd0a12ca7d7696905c854830cc4.

- 2026-10-08T08:45:38+00:00: Recorded command exit 0; command argv SHA-256
  5aa618a5ddc4f2bb88a23a91dbcff6274a6679f52d5a8d8a209595c235a72718.

- 2026-10-08T08:46:12+00:00: Recorded command exit 0; command argv SHA-256
  72078c00e32013db11dd2260bec9df4023e631fbcec73afa011079568529015e.

- 2026-10-08T08:46:36+00:00: Recorded command exit 0; command argv SHA-256
  afde301339936552309a78676f099fc4fdb98e82ba2ee2c62052c3cfbf614206.

- 2026-10-08T08:46:58+00:00: Recorded command exit 0; command argv SHA-256
  736b8377c05a760d5a5653b5fbacd0cfc8e277ac3f52039139fde5f52f7ad908.

- 2026-10-08T08:48:09+00:00: Recorded command exit 0; command argv SHA-256
  23921d95a4e6313b6b5e84de12bdb21031bf3486022cb27e42b55623a038ed7f.

- 2026-10-08T08:48:52+00:00: Recorded command exit 0; command argv SHA-256
  be634c03ce99074b1f3ac0dfe8f2ebebb66aa8608db002fa5e5582a4cbc283ff.

- 2026-10-08T08:49:09+00:00: Recorded command exit 3; command argv SHA-256
  1031aacf308f2b74bfcc5df28839dbde069363eb1e13c2c700aaf3f6ba7d0f5c.

- 2026-10-08T08:49:30+00:00: Recorded command exit 0; command argv SHA-256
  aad48328738b7ce945f00caa5a62efd3be0e53b8ff082903e2e7fdf153c80607.

- 2026-10-08T08:49:51+00:00: Recorded command exit 0; command argv SHA-256
  7f028348ee9983ef79ed59ea74099c0a3106153767301da199b56bd4eb58ac6b.

- 2026-10-08T08:51:35+00:00: Recorded command exit 101; command argv SHA-256
  f091e450d360944faa933b1491cbfeb580aeb1e919af536774ef0b19468ee812.

- 2026-10-08T08:51:52+00:00: Recorded command exit 0; command argv SHA-256
  f93526e817a0475c7e882bdccf3c8abc7c6acc3a6f47a2acebaa93f458f51485.

- 2026-10-08T08:52:42+00:00: Recorded command exit 0; command argv SHA-256
  29f19b8759e5dfc0d33b8b848c3c61dcb5fc21f1d2734363d3359371966c9e47.

- 2026-10-08T08:52:59+00:00: Recorded command exit 0; command argv SHA-256
  4dfca3829cea04ac951dabd8508fc29271afae8cca33fe05dc0102aa20a90e8a.

- 2026-10-08T08:53:14+00:00: Recorded command exit 0; command argv SHA-256
  1e9924c5837a7b5438ff0117a8c5023c59f270f4ad53c03b56e9dafaf50670ad.

- 2026-10-08T08:53:32+00:00: Recorded command exit 1; command argv SHA-256
  a77ce49de85c4f40f7653d5efbaa4d9109d53c60290e43e295220883d14b3d06.

- 2026-10-08T08:55:26+00:00: Recorded command exit 0; command argv SHA-256
  f091e450d360944faa933b1491cbfeb580aeb1e919af536774ef0b19468ee812.

- 2026-10-08T08:56:48+00:00: Recorded command exit 0; command argv SHA-256
  793c8e4c8e7cc23ae6ec9b294d10994590cacb3837e6e8667d51ec86b1cb8efb.

- 2026-10-08T08:57:22+00:00: Recorded command exit 0; command argv SHA-256
  76cd43656a16f72d6d7926c7a98fd26ffc272ad222834fac80c98e646f04687b.

- 2026-10-08T08:57:49+00:00: Recorded command exit 0; command argv SHA-256
  9e2dc21d5886b88e740d62819d38e42049d2009b08cc6e5557d0b3683e735266.

- 2026-10-08T08:58:13+00:00: Recorded command exit 0; command argv SHA-256
  110d45e7be1e719ac22e293a722d351a05b1122c97d6e3bb6d37ca24c010569d.

- 2026-10-08T08:58:31+00:00: Recorded command exit 0; command argv SHA-256
  6d9217d60161bc0bc1fbf4e7a26b3155c558515bac748df0478c063c6cb0b7a5.

- 2026-10-08T08:58:44+00:00: Implemented TUI-only bounded owner Rustup layout acceptance with
  descriptor-bound Cargo/Rustc, persistent warning, hostile-path tests, legacy compatibility, and
  detached wrapper ref forwarding. Full locked suite and exact candidate host/fresh-user journey
  pass; PR #293 opened.

- 2026-10-08T08:58:54+00:00: Recorded command exit 0; command argv SHA-256
  7e9a097df169bd1d040d17f89f79ec1f7d01625c542199b091f7a2e90defb19b.

- 2026-10-08T08:59:06+00:00: Recorded command exit 0; command argv SHA-256
  697075b0f6df384db27f2c1e0ed779c3ff2da103e22a4b524a8659d7b08ffb05.

- 2026-10-08T08:59:23+00:00: Recorded command exit 0; command argv SHA-256
  61f1bde25a9eba54d5a018ce00dd0ffab439477943af80107fbe8ed468b65142.

- 2026-10-08T08:59:35+00:00: Recorded command exit 0; command argv SHA-256
  2ba60873574f01105c07d2830d50c17807560a52c2a824a5b95918f52f64f1fd.

- 2026-10-08T08:59:47+00:00: Recorded command exit 0; command argv SHA-256
  1a4e96e7d3f2fa0b16645d89bd0ba3893e0fb91447b5f059d952332cf95ae4cb.

- 2026-10-08T09:00:07+00:00: Recorded command exit 0; command argv SHA-256
  9fb7f3bf61dfeee7d0f3b635ae3b35b22c5f2b7eb0eb1f7e212742a52346c875.

- 2026-10-08T09:00:20+00:00: Recorded command exit 0; command argv SHA-256
  98080e54c1c4b2adf3be51010daa7c07df704e45dd78736f0c2d8bf3c86badba.

- 2026-10-08T09:00:36+00:00: Recorded command exit 0; command argv SHA-256
  822e5d76116a5a1e595bd0c3fb14c846149b1c6633d471e484f60ba90442e0c6.

- 2026-10-08T09:00:48+00:00: Recorded command exit 1; command argv SHA-256
  76e6aadf04c27bf91bc8c9682ac4d55ba2c5b5aefc2dafdc082e7bb7a66bc9e5.

- 2026-10-08T09:00:59+00:00: Recorded command exit 2; command argv SHA-256
  e40731aba2c6476ab4e37b682a30f7b85e2e817d313ee372e69383d50684dde4.

- 2026-10-08T09:01:18+00:00: Recorded command exit 0; command argv SHA-256
  9161b7ed9cd132e21eae7d72ab7ba30a6863305c12ae27ada4a4638a93c661aa.

- 2026-10-08T09:01:30+00:00: Recorded command exit 101; command argv SHA-256
  e54fc704655694f6555665e45263e1e4730760fa8a998829e1497c42bb6f1839.

- 2026-10-08T09:01:44+00:00: Recorded command exit 0; command argv SHA-256
  9073a16d976b2006a61a468cd14720bfca57b98a62d8f1b838ea7a184eeeba16.

- 2026-10-08T09:02:18+00:00: Recorded command exit 0; command argv SHA-256
  519cf549ade86cf4c5f9a2b15ad63d9e9fde379a72cb778e38791be735a33ebb.

- 2026-10-08T09:02:27+00:00: Recorded command exit 0; command argv SHA-256
  53dbda2e9fa002833ddbf0c0df02038755133373e889937d3b34d840df24cf1b.

- 2026-10-08T09:02:39+00:00: Recorded command exit 0; command argv SHA-256
  14f8b77e963848e8633fa90ef078bcff6f20d0909831a08f9ab327473e9a27a4.

- 2026-10-08T09:02:51+00:00: Recorded command exit 1; command argv SHA-256
  2bd31db781c5c321580c71990621d739b7710613357fe13494da01f72bf6dcee.

- 2026-10-08T09:03:03+00:00: Recorded command exit 0; command argv SHA-256
  8e47b4fa295ea60aaac4de15488a640927fffe199886c817c7a976c26265c6d4.

- 2026-10-08T09:03:15+00:00: Recorded command exit 0; command argv SHA-256
  641f8eb1df0e02b855a2f61277d390afddba6be7ec796c189a706cbc225a2688.

- 2026-10-08T09:03:28+00:00: Recorded command exit 0; command argv SHA-256
  0271b28e6b1a026fee00b376cbc3d7227f6af024c9875c8c2363726eacf0f799.

- 2026-10-08T09:03:42+00:00: Recorded command exit 0; command argv SHA-256
  4fc80585a85b5cf98f34dfcd8a45e505761ea959b6ac7a8637db3282028ca418.
