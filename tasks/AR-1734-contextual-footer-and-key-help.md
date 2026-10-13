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
  "next_action": "Obtain independent exact-head review of PR #302 and repair any findings before merge.",
  "observed_branch": "feature/ar1734-contextual-footer-hotkeys",
  "observed_dirty": 0,
  "observed_head": "f7b6bb84c6ff3de6a690a213aeb4cb5056bc598c",
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
  "task_revision": 84,
  "title": "Render contextual footer help and current hotkeys",
  "updated_at": "2026-10-13T01:25:20+00:00",
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

- 2026-10-13T01:12:51+00:00: Recorded command exit 1; command argv SHA-256
  9dc63170564a0f181b0d46e133ce69aeb6772c4de967b171ec540b95d1a835e2.

- 2026-10-13T01:13:08+00:00: Recorded command exit 0; command argv SHA-256
  6c5d36898918a9288e73f9f39b2e3672acf6de315d6787074fbc48ef563cce08.

- 2026-10-13T01:13:16+00:00: Recorded command exit 1; command argv SHA-256
  742f2052dd42b002f8d6897f41c843dc4c4e9be7c5d6cdb5120aad1d0711c438.

- 2026-10-13T01:15:16+00:00: Recorded command exit 1; command argv SHA-256
  6e6dc963a3595b34c14b0ac12f9a21bfe64d00f0a1e249cd7a4579bd73137bc2.

- 2026-10-13T01:15:29+00:00: Recorded command exit 0; command argv SHA-256
  183cc59e9127db6e4c9b978864c05e67254c56da9a552e76ac968aedd8c3ff5f.

- 2026-10-13T01:15:38+00:00: Recorded command exit 0; command argv SHA-256
  31495f68c94f752061a31c97e976b715450d23612fd562bc300467e11f11b9b1.

- 2026-10-13T01:16:11+00:00: Recorded command exit 2; command argv SHA-256
  9ec8886fbc6e525c292a4bca504764a7a6a7405ba7a883580cd1ac15b48b96d2.

- 2026-10-13T01:16:23+00:00: Recorded command exit 0; command argv SHA-256
  c6c901ede0b33bbadb272d822248cad251564a7f9cade2ce66bde7aafe1e82ff.

- 2026-10-13T01:16:38+00:00: Recorded command exit 1; command argv SHA-256
  4275a02b40a5564a7e2b7c908cb1e0fb031a467cafb65136eb4ec2fb602d8f77.

- 2026-10-13T01:16:47+00:00: Recorded command exit 0; command argv SHA-256
  f777125df45ade5c78b1f4bd21338d3deb9eb1a6146b3eb4273d2f97dbb63911.

- 2026-10-13T01:18:39+00:00: Recorded command exit 0; command argv SHA-256
  cf203eba4c99e9b2468ba9fe1aa936aa33a1bb8f599e52acf4831536b90cb088.

- 2026-10-13T01:18:53+00:00: Recorded command exit 2; command argv SHA-256
  f9628fec6f488b34f7b45679e692e302d3fced5c70c60cea9232cb0e68a16b18.

- 2026-10-13T01:19:07+00:00: Recorded command exit 1; command argv SHA-256
  aeb4de85306e6b9ab52a6ecf1eb421ebe95d574e196b32e162d3b8365e9d084d.

- 2026-10-13T01:19:21+00:00: Recorded command exit 0; command argv SHA-256
  a9bbd2fc1de80b2778c8f9e5d54f9bc57708e2cff926bbf948bbfa7dcc137f82.

- 2026-10-13T01:19:32+00:00: Recorded command exit 0; command argv SHA-256
  f6b2709ea41ea1ebebd11a9c427f0e6cdff627240e16ccd8f24a1573f39a506c.

- 2026-10-13T01:19:44+00:00: Recorded command exit 0; command argv SHA-256
  1cee5ee50bb844c22844af4be7d84d4aba9e04389c5c1cc8cb3eebb0c06fadd3.

- 2026-10-13T01:20:23+00:00: Implemented complete contextual footer/help overlay scope on signed+DCO
  head f7b6bb84c6ff3de6a690a213aeb4cb5056bc598c; opened
  https://github.com/martin-beck/asb-tui/pull/302. Full cargo tests, clippy, fmt, docs, release
  build, model/help/source-parity validators, gitleaks, and clean coverage at 90.04% passed locally.
  cargo-deny and cargo-audit were unavailable locally and remain hosted-CI gates. No merge
  performed.

- 2026-10-13T01:20:29+00:00: Recorded command exit 0; command argv SHA-256
  c802299eca09f59fb0ce088395b222e4a9b7bbe8527dd860af4c44d6e0c3aea3.

- 2026-10-13T01:23:22+00:00: Recorded command exit 0; command argv SHA-256
  cb8267f2d102457deecbb36448f1f7853826f9b208cada1d3184445d3f71b862.

- 2026-10-13T01:23:31+00:00: Recorded command exit 8; command argv SHA-256
  edd0b2e431d2ec77df34e3863f6a89f61a5c081f964eec0642fe1a4bd4d43f98.

- 2026-10-13T01:25:20+00:00: Recorded command exit 0; command argv SHA-256
  b19e54073a5054a2cf311a8b12b8597c72989a74fdb78bc303a57db0d39edcd3.
