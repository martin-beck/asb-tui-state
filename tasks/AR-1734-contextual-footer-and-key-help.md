---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T02:50:24+00:00",
  "depends_on": [
    "AR-1731",
    "AR-1732",
    "AR-1733"
  ],
  "id": "AR-1734",
  "next_action": "Render focus-aware concise footer help and a discoverable context-sensitive hotkey overlay for every current element and action.",
  "observed_branch": "feature/ar1734-contextual-footer-hotkeys",
  "observed_dirty": 12,
  "observed_head": "486d24709d9045d8e4e2d91221db3a754d2fe3b6",
  "owner": "codex-asb-tui-ar1734-context-help-20261013",
  "plan": "../plans/AR-1734-contextual-footer-and-key-help.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1734.json",
    "spec_revision": 1,
    "status": "planned"
  },
  "spec_ref": "specs/AR-1734.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add a context-sensitive footer and hotkey overlay that explain the highlighted or hovered item and available actions.",
  "task_revision": 59,
  "title": "Render contextual footer help and current hotkeys",
  "updated_at": "2026-10-13T01:10:53+00:00",
  "worktree_key": "asb-tui-ar-1734-contextual-footer-hotkeys"
}
---

Existing document-backed help remains authoritative. This AR makes that help
immediately usable in the visual shell, rather than requiring a separate
documentation lookup.

- 2026-10-13T00:45:20+00:00: AR-1731 through AR-1733 are released; contextual help implementation is
  dependency-ready.

- 2026-10-13T00:45:22+00:00: Claimed by codex-asb-tui-ar1734-context-help-20261013.

- 2026-10-13T00:45:59+00:00: Recorded command exit 0; command argv SHA-256
  721c4b9bdc49e1801fc3f3209141a743a35a35512058546e7aad2aeb5abc78f2.

- 2026-10-13T00:50:24+00:00: Heartbeat by codex-asb-tui-ar1734-context-help-20261013.

- 2026-10-13T00:54:01+00:00: Recorded command exit 0; command argv SHA-256
  76685490e86e9373ebf5d43af76e36c0d28823c1efc04e24b8d14f7eac7b9753.

- 2026-10-13T00:54:27+00:00: Recorded command exit 0; command argv SHA-256
  0b30f478cca8cd341e53d85eb2a0d66788d12937fb2b90a8cf095ae627232829.

- 2026-10-13T00:55:02+00:00: Recorded command exit 0; command argv SHA-256
  8410dcd279540673995bfa291dadace5951248196be77d93b573bf114a7d1511.

- 2026-10-13T00:55:12+00:00: Recorded command exit 0; command argv SHA-256
  0766b3bf003f416cd334c74ad52955af585153bfc2803d2395f1ce97beeb2b01.

- 2026-10-13T00:55:31+00:00: Recorded command exit 0; command argv SHA-256
  eb244986dd8e619f0bda97db9bc47c00ae72e2de816ec157fe2a20d63b32c503.

- 2026-10-13T00:56:03+00:00: Recorded command exit 0; command argv SHA-256
  84e25ef99708bae6b11ea615ed0281c790c75401a8a22bdc7aa88440b3277111.

- 2026-10-13T00:56:16+00:00: Recorded command exit 0; command argv SHA-256
  c9797974d95d1890c932ed386d14372e26d3e99ee2f448ed06933cb34f2d047f.

- 2026-10-13T00:56:25+00:00: Recorded command exit 0; command argv SHA-256
  eb244986dd8e619f0bda97db9bc47c00ae72e2de816ec157fe2a20d63b32c503.

- 2026-10-13T00:57:25+00:00: Recorded command exit 0; command argv SHA-256
  53b81d16679ce3dcf0ac56896c169fffe3634a994568754efa9d0c5dbb1797f9.

- 2026-10-13T00:57:51+00:00: Recorded command exit 0; command argv SHA-256
  dc92cc3cf274040fdbd109be0f61d8778fc2a64f7902fb06e89223917015aeee.

- 2026-10-13T00:58:00+00:00: Recorded command exit 1; command argv SHA-256
  970fc560e835a6570640ba7a119349a8fd278882c0862e2ac19871ffc049d16a.

- 2026-10-13T00:58:38+00:00: Recorded command exit 0; command argv SHA-256
  4aa464e9e80b13b6f5fa466bec84086d142e23670d7da5153fddfbc4e545d850.

- 2026-10-13T00:58:47+00:00: Recorded command exit 1; command argv SHA-256
  fc876b2e223d9a62de935b55ec21639b7d5fcdccb753618dc1fe5284ade91bc9.

- 2026-10-13T00:59:14+00:00: Recorded command exit 0; command argv SHA-256
  e58630bf5de1fa8dbd8912faeb8533a447fd520a80eb78dd1a7bf6c4fdc10b76.

- 2026-10-13T00:59:23+00:00: Recorded command exit 1; command argv SHA-256
  d1f8894347fcca4fd613f6a6b3fcab16bde98c9390a2226d86b8bd315fb75e51.

- 2026-10-13T00:59:55+00:00: Recorded command exit 0; command argv SHA-256
  f1f114c4a08d40fead3912026370e4dd6ba390ffeac9bfa03b3a788704487799.

- 2026-10-13T01:00:05+00:00: Recorded command exit 1; command argv SHA-256
  bef02727a0e8d1c1cca3e03ce292e588ef56bc05deac4a0cffbe5dc2bd625d56.

- 2026-10-13T01:00:19+00:00: Recorded command exit 0; command argv SHA-256
  af8f87fcc966ae42d1cadd852a1954347ae73672ae5203b01f0d8066cf9921b4.

- 2026-10-13T01:00:34+00:00: Recorded command exit 0; command argv SHA-256
  bbd85ff444aed19bde932746d84921fd6a5640bdb5beb3a062af56b5f7fd3d77.

- 2026-10-13T01:00:46+00:00: Recorded command exit 1; command argv SHA-256
  2f0b27c8b15f0c468aff0910ac303a09aa6997af0af597dc824a2df9146ddd93.

- 2026-10-13T01:01:07+00:00: Recorded command exit 101; command argv SHA-256
  317df2111ebfb38b5cf798f894c5352bdbe345ba7c5b58c157beb2e29932727f.

- 2026-10-13T01:01:26+00:00: Recorded command exit 0; command argv SHA-256
  ea1e1ab3dcf6107eff315fba32a5b1fae3707d2e425e8d304d8ed870b645d3e1.

- 2026-10-13T01:01:53+00:00: Recorded command exit 0; command argv SHA-256
  a8ecfc4663e48a83300f8276b19bb25798316c28c83647f2fc3cd24ee9cb61da.

- 2026-10-13T01:02:21+00:00: Recorded command exit 101; command argv SHA-256
  6a07014bed9331db373657062c5433645ad73ff53ca6fd8512e6a2cb02c11a19.

- 2026-10-13T01:02:36+00:00: Recorded command exit 101; command argv SHA-256
  3d8c462bca83731cf4563835905a94274c8fe51e0929cd9256d2f71a946f0c94.

- 2026-10-13T01:03:05+00:00: Recorded command exit 101; command argv SHA-256
  63780507c2dc648ca219df5a1c264fcf62f7a74fee1df428f2888bb62aa3bef1.

- 2026-10-13T01:03:18+00:00: Recorded command exit 101; command argv SHA-256
  58a271ef47a7dc1f6afd790b1fa79cfc877caa1f7eaea561202884e1c737bae5.

- 2026-10-13T01:03:34+00:00: Recorded command exit 0; command argv SHA-256
  1be82361cebfbe57af24df8e8c360d74e8c4be28624e5ba55eff657a4e753c26.

- 2026-10-13T01:03:55+00:00: Recorded command exit 0; command argv SHA-256
  4e509dee56c301749e2929905a610d04c86c95ae554099707bbcfd44b63698e2.

- 2026-10-13T01:04:23+00:00: Recorded command exit 101; command argv SHA-256
  d18f059de05b295fdb99d2711593e1ab6c530967f3e4addaf203a9239cfaad8f.

- 2026-10-13T01:04:41+00:00: Recorded command exit 0; command argv SHA-256
  9fc491beb96cec92f643336f28a7468cf87127a55805ab168187cd69a485d60c.

- 2026-10-13T01:04:59+00:00: Recorded command exit 101; command argv SHA-256
  1a3777fc4519281deff1cc4f85689b38591bb3c7cd7bcb4694c02a3b8874f3f7.

- 2026-10-13T01:06:14+00:00: Recorded command exit 101; command argv SHA-256
  cd7f82c74af6e98e5bc198837e2c96c2447fa6a6bacb4dadc97c4e4fa6f6d494.

- 2026-10-13T01:06:24+00:00: Recorded command exit 0; command argv SHA-256
  2bb6e728854bd070ade66c2549f1f2d2769ae97500ede1bc642ed330825f7823.

- 2026-10-13T01:08:09+00:00: Recorded command exit 0; command argv SHA-256
  1a3777fc4519281deff1cc4f85689b38591bb3c7cd7bcb4694c02a3b8874f3f7.

- 2026-10-13T01:08:21+00:00: Recorded command exit 1; command argv SHA-256
  5be0847724ba8e38ac73070f0af9b64e0c645ed202dfd5d3eb2d6e61c6a5e307.

- 2026-10-13T01:09:37+00:00: Recorded command exit 0; command argv SHA-256
  92909439b042735221bd04f1e3eb60b390c456737acf8d807c294980c286348e.

- 2026-10-13T01:10:00+00:00: Recorded command exit 101; command argv SHA-256
  6da093a9e1a47467415e8bf200669a3da94bd348c0eb9841b36ce12613c1ae9c.

- 2026-10-13T01:10:12+00:00: Recorded command exit 1; command argv SHA-256
  742f2052dd42b002f8d6897f41c843dc4c4e9be7c5d6cdb5120aad1d0711c438.

- 2026-10-13T01:10:19+00:00: Recorded command exit 1; command argv SHA-256
  c670a8eb9b58b7fb2e66af86f19a80106f33eb996833ae15ddfe97ca69cc46b2.

- 2026-10-13T01:10:53+00:00: Recorded command exit 0; command argv SHA-256
  4a4f244b4b66b4433f54b91fa8c938ed98f5e064a5665539917b6fa105bcb801.
