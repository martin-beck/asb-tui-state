---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1723"
  ],
  "id": "AR-1731",
  "next_action": "Define and implement the renderer-neutral visual language and persistent wizard shell before changing individual controls.",
  "observed_branch": "feature/ar1731-visual-language-shell",
  "observed_dirty": 0,
  "observed_head": "97e6692946c3d91b3f4964b9f6a556673bdc35c8",
  "owner": "",
  "plan": "../plans/AR-1731-visual-language-and-wizard-shell.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "sha256:fe05186212b96350beb3638b2dcd9ee4df4849b58e2c39c5ced3e8a216afe1b0",
    "evidence_ref": "quality/AR-1731-postmerge-receipt-20261012.json",
    "spec_ref": "specs/AR-1731.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1731.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Create a professional, accessible ASB TUI visual language and persistent wizard shell informed by established high-value terminal UIs.",
  "task_revision": 45,
  "title": "Establish ASB TUI visual language and wizard shell",
  "updated_at": "2026-10-12T22:52:24+00:00",
  "worktree_key": "asb-tui-ar-1731-visual-language-shell"
}
---

Create the shared visual vocabulary used by every ASB TUI route. Reference
widely understood terminal UI conventions exemplified by k9s/lazygit-style
focused panes, status colors, compact key hints, and readable borders, without
copying their code, marks, or assets.

- 2026-10-12T22:13:51+00:00: AR-1723 is done; the merged visual-fidelity series makes this first
  implementation task dependency-ready.

- 2026-10-12T22:13:54+00:00: Claimed by codex-asb-tui-ar1731-visual-20261013.

- 2026-10-12T22:16:47+00:00: Recorded command exit 0; command argv SHA-256
  f74c7cab610b86d7e3f79428ee8b1e08bd01ec2c912c7cf2ba3806c3d7e68d3b.

- 2026-10-12T22:16:52+00:00: Recorded command exit 0; command argv SHA-256
  956e570bcfe4c748aac40c0102ba799553996b15566a0e5e6940ab9b170d713a.

- 2026-10-12T22:18:42+00:00: Recorded command exit 0; command argv SHA-256
  95a52830db9f355fc72fa689a97a77fbc602f13ba9d3567ffe923ba04e46dbb2.

- 2026-10-12T22:22:22+00:00: Recorded command exit 0; command argv SHA-256
  53473b080f44603688f459425641f7c91dfa6e2c1192d725ac27e5615cb8c46d.

- 2026-10-12T22:22:29+00:00: Recorded command exit 0; command argv SHA-256
  539176617c45ae92a87de61fe42ae8b94021cbfa8c65b36509ed65e67edd9570.

- 2026-10-12T22:22:56+00:00: Recorded command exit 101; command argv SHA-256
  54a5c9543101ec081dd9223150c8ee1ea70aabdd76ec07781574bb3e6e2b1c1a.

- 2026-10-12T22:23:09+00:00: Recorded command exit 0; command argv SHA-256
  6d70f94c4c9ca3af506d7244c0887c52aa3b5f4e26e4e7da076ca79e24fb08a8.

- 2026-10-12T22:23:13+00:00: Recorded command exit 0; command argv SHA-256
  680aee40c59702fc1dec5e5473d0083b79a4ea4a90cbaa42a0a728d0d58b389d.

- 2026-10-12T22:23:18+00:00: Recorded command exit 0; command argv SHA-256
  c3e5f0c041ed09cb25d016283a7b780fa3bc80719ee665d0487801558e05ae5b.

- 2026-10-12T22:23:23+00:00: Recorded command exit 0; command argv SHA-256
  dbb2755004cc88ea7190c700e7d511937de5f802f6844f9cef5fedc0050aacd5.

- 2026-10-12T22:23:28+00:00: Recorded command exit 0; command argv SHA-256
  14b6804ccd4ca9a754b183b0d54c2bd695c69c75e367d50449cc94a75eb2b880.

- 2026-10-12T22:23:51+00:00: Recorded command exit 0; command argv SHA-256
  54a5c9543101ec081dd9223150c8ee1ea70aabdd76ec07781574bb3e6e2b1c1a.

- 2026-10-12T22:23:56+00:00: Recorded command exit 0; command argv SHA-256
  14b6804ccd4ca9a754b183b0d54c2bd695c69c75e367d50449cc94a75eb2b880.

- 2026-10-12T22:24:02+00:00: Recorded command exit 0; command argv SHA-256
  314dd08929dc01db73696d95dbee0ae8303deb9b08a8dfc25d979d48e67b78b3.

- 2026-10-12T22:24:07+00:00: Recorded command exit 0; command argv SHA-256
  dbb2755004cc88ea7190c700e7d511937de5f802f6844f9cef5fedc0050aacd5.

- 2026-10-12T22:25:07+00:00: Recorded command exit 0; command argv SHA-256
  1dd150209b503970bf550a22c9dbcc7f308c45f641cb256d1a81a58997e87c72.

- 2026-10-12T22:25:23+00:00: Recorded command exit 101; command argv SHA-256
  66f74c480ee98b2b5cea79ec360bbfd39bdd424869ee67506c7d83f010064f73.

- 2026-10-12T22:26:13+00:00: Recorded command exit 0; command argv SHA-256
  53473b080f44603688f459425641f7c91dfa6e2c1192d725ac27e5615cb8c46d.

- 2026-10-12T22:26:19+00:00: Recorded command exit 0; command argv SHA-256
  66f74c480ee98b2b5cea79ec360bbfd39bdd424869ee67506c7d83f010064f73.

- 2026-10-12T22:26:45+00:00: Recorded command exit 101; command argv SHA-256
  4e32c2c40f73fe4ec370f5682ab96df7305786e75b24bf93391381c4ba2cb77c.

- 2026-10-12T22:30:27+00:00: Recorded command exit 101; command argv SHA-256
  862b47cbb47aba95a9965ebc423f5fe69c30e4aedcc3c7b3036f1dc232bbbfb9.

- 2026-10-12T22:31:50+00:00: Recorded command exit 0; command argv SHA-256
  fac77509eb6764f2a6433a69775f1145d1747d5801a434130dae24f9b410f3c1.

- 2026-10-12T22:33:54+00:00: Recorded command exit 0; command argv SHA-256
  e7218b52b0b3a5ec0465880cc59e0039e5c8d1c917b20f1db53bf9a85ffde36e.

- 2026-10-12T22:34:58+00:00: Recorded command exit 1; command argv SHA-256
  8b841414208f8dae6f9916f41ce4d0a48f9e31344c0fda080ab65a586b2aa4f0.

- 2026-10-12T22:35:16+00:00: Recorded command exit 0; command argv SHA-256
  b55f76d002e3d3bcb8e6452fd0b9f9c75f8836c549088cdb856a202e41ddc946.

- 2026-10-12T22:36:21+00:00: Recorded command exit 0; command argv SHA-256
  b4ff0ba01bb740c9c59fff610c143560f3a01c820821d29ab5274c238e59c9d3.

- 2026-10-12T22:36:26+00:00: Recorded command exit 0; command argv SHA-256
  8297c34cee3ffd25a4b6e04f779735f08ce4eeb200d3bdc5f3315a538fd95284.

- 2026-10-12T22:36:41+00:00: Recorded command exit 0; command argv SHA-256
  ba9afa7580c3753b33b10d509b2d89aab0a7aa3bbe8f33165bb1260cbb239a86.

- 2026-10-12T22:36:46+00:00: Recorded command exit 0; command argv SHA-256
  2258721d73c228427413be69b7ec00283a390d3be62613e5dc688e99af80953c.

- 2026-10-12T22:37:08+00:00: Recorded command exit 0; command argv SHA-256
  483bed92ab617be0e89e20506e004d0824e34e846f0eade5ad3f8e85277ce451.

- 2026-10-12T22:37:39+00:00: Recorded command exit 0; command argv SHA-256
  a7bedef34811a907f49ab2ac7b4f520061e9fce32a4fc5527f4d693100712bbb.

- 2026-10-12T22:38:01+00:00: Recorded command exit 0; command argv SHA-256
  f6551ce073cda841b77e4691e4df9eff66b5b2b1fb1be25452ddcbd40bf08cb7.

- 2026-10-12T22:44:54+00:00: Recorded command exit 0; command argv SHA-256
  add9e568d30c374e016ea7be4a60660553cc6801f9b6efed408cede65b9001cf.

- 2026-10-12T22:52:01+00:00: Recorded command exit 0; command argv SHA-256
  cd4baf5d08da969aef20a1734c6895d3e39e94a7a9325e707f894d3bfd83c909.

- 2026-10-12T22:52:08+00:00: Recorded command exit 0; command argv SHA-256
  fbecca1c1c8e5eb0fa7b6d564acfc7784f3248330f19218eb17631afbe7e4f1b.

- 2026-10-12T22:52:21+00:00: AR-1731 merged at 4fd9d2b and exact-main quality and trusted-main runs
  succeeded.

- 2026-10-12T22:52:24+00:00: Released after recorded exact-main qualification.
