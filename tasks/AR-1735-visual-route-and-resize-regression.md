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
  "next_action": "Add deterministic visual-route, resize, accessibility, and formal parity regression coverage for the new fidelity system.",
  "observed_branch": "feature/ar1735-visual-route-resize-regression",
  "observed_dirty": 8,
  "observed_head": "3d978ba716f17ed9c11ca7f732c646e68a06ab7f",
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
  "task_revision": 44,
  "title": "Qualify visual fidelity across routes, resize, and terminal capabilities",
  "updated_at": "2026-10-13T02:44:04+00:00",
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
