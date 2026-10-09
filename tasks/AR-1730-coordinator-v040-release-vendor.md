---
{
  "branch": "upgrade/ar-1730-coordinator-v0.4.0-release",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T20:46:52+00:00",
  "depends_on": [],
  "id": "AR-1730",
  "next_action": "Full locked state suite passes 270 tests in the offline uv environment with jsonschema 4.25.1; vendor/source/tree/mode/digest, headers, doctor, render-status, gitleaks, diff, and commit-policy gates pass. Rebase signed candidate onto current pushed main, obtain independent exact-tree review, and publish PR.",
  "owner": "codex-asb-tui-ar1730-v040-20261009",
  "plan": "../plans/AR-1730-coordinator-v040-release-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1730.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the exact Agent Workflow Coordinator v0.4.0 release and qualify ASB-TUI state compatibility without patching vendored bytes or weakening provenance gates.",
  "task_revision": 39,
  "title": "Coordinator v0.4.0 release vendor for ASB-TUI compatibility",
  "updated_at": "2026-10-09T17:58:25+00:00",
  "worktree_key": ""
}
---

The ASB-TUI state repository currently vendors Coordinator development commit
`e863b57edc7f7a21b2aff2c7b45ce226e12637d2`. Upstream now exposes the exact
`v0.4.0` release at commit `712b36ea3d188237cbe8104e70d905094f93a96b`, tree
`c496306050a805111f89b3f7bc4cfb0910f27535`. The remote tag is lightweight;
this AR records that limitation and does not claim an annotated tag signature.

This AR owns only the ASB-TUI state vendor and downstream compatibility. It must
preserve the project binding, Git backend, task lifecycle, privacy policy,
generated views, and source-only product boundary. No ASB product/state or
unrelated repository may be changed.

- 2026-10-09T17:46:47+00:00: Defined exact Coordinator v0.4.0 release vendor and ASB-TUI
  compatibility scope; upstream commit/tree and lightweight-tag boundary recorded.

- 2026-10-09T17:46:52+00:00: Claimed by codex-asb-tui-ar1730-v040-20261009.

- 2026-10-09T17:47:02+00:00: Recorded command exit 129; command argv SHA-256
  9c83eec5a6380eaa4f352108892294ce1a0aa1d78ca8fb6d7c0f94d3a45b69a7.

- 2026-10-09T17:47:12+00:00: Recorded command exit 0; command argv SHA-256
  604f493bb7255edc0fa98ef1910c6badad29e2fedfba4cc23c1449a01f36bc76.

- 2026-10-09T17:47:44+00:00: Recorded command exit 0; command argv SHA-256
  552c147938c0a0429bbf5dc20d61bb1650d78e8ffe1aa455250146181ab73110.

- 2026-10-09T17:47:55+00:00: Promotion, claim, stale-worktree cleanup, reconcile, live doctor, and
  exact isolated branch setup passed; state main is pushed.

- 2026-10-09T17:48:00+00:00: Recorded command exit 0; command argv SHA-256
  552c147938c0a0429bbf5dc20d61bb1650d78e8ffe1aa455250146181ab73110.

- 2026-10-09T17:48:12+00:00: Recorded command exit 0; command argv SHA-256
  8ad2e7c9365b3c127312944ae9f94b740b4869832ef9834d8db463abb98943d3.

- 2026-10-09T17:48:35+00:00: Recorded command exit 0; command argv SHA-256
  9f2798e49383259f5297520203ab32d0870ccf88e178309c870de02a091145fa.

- 2026-10-09T17:48:52+00:00: Recorded command exit 0; command argv SHA-256
  0c7f8e1be4ccc5838aac6f634d055ac65576f25bb0ffc4179b5c4c2fb54959d7.

- 2026-10-09T17:49:01+00:00: Recorded command exit 1; command argv SHA-256
  d1f87da15ae0640e09a17fef651aab1336139e9ca3fe17eda3c606749601e61f.

- 2026-10-09T17:49:10+00:00: Recorded command exit 0; command argv SHA-256
  ec1a8bfcb82d6f6633e68ab1d2658a3bc31c9cd56a128b3324edfb49b366240c.

- 2026-10-09T17:49:25+00:00: Recorded command exit 0; command argv SHA-256
  55584feedbeb9001db912318b1551b4855f74d32600e1b8450b915a3875c9bb3.

- 2026-10-09T17:51:06+00:00: Recorded command exit 0; command argv SHA-256
  e174402599f3a3b4e0e4048849081d9c2539469581bd4f36d76c7b79af00db2f.

- 2026-10-09T17:51:56+00:00: Recorded command exit 1; command argv SHA-256
  42d23f3d823d2e1fe9d84ff4e72d048117e752818dceec7ccfd52d08a65a6ef0.

- 2026-10-09T17:52:10+00:00: Recorded command exit 0; command argv SHA-256
  31e58aeacc755d596df9a6023607ef9c4b4196e476165c3c7341754c5a9eca09.

- 2026-10-09T17:52:16+00:00: Recorded command exit 0; command argv SHA-256
  ec1a8bfcb82d6f6633e68ab1d2658a3bc31c9cd56a128b3324edfb49b366240c.

- 2026-10-09T17:52:21+00:00: Recorded command exit 1; command argv SHA-256
  1f99de6d954eb1f1e262bbca198e7ea3f53ec812b93bf76557f97bfc2caca98c.

- 2026-10-09T17:52:32+00:00: Recorded command exit 0; command argv SHA-256
  6d2372f92b08f161cd0fad9d11998d28c827eee91c6b245d9e940bdbf7209c38.

- 2026-10-09T17:52:55+00:00: Recorded command exit 0; command argv SHA-256
  6d2372f92b08f161cd0fad9d11998d28c827eee91c6b245d9e940bdbf7209c38.

- 2026-10-09T17:53:12+00:00: Release vendor verifier, source/tree comparison, headers, focused
  Git-backend tests, doctor, and render-status pass. Full suite has only two import errors because
  host lacks jsonschema; no vendor assertion remains. TLC correctly fails closed without
  systemd-run.

- 2026-10-09T17:53:18+00:00: Recorded command exit 0; command argv SHA-256
  552c147938c0a0429bbf5dc20d61bb1650d78e8ffe1aa455250146181ab73110.

- 2026-10-09T17:53:59+00:00: Recorded command exit 0; command argv SHA-256
  a4a0db3cc1e6ce03d028b01285e263562f6cde50a16c3f55b786ae9216d320a5.

- 2026-10-09T17:54:11+00:00: Recorded command exit 0; command argv SHA-256
  9d9f2395274d0493cb7f2d9bddbea9039ec171616246be77f6c4aeceead9a8b3.

- 2026-10-09T17:54:39+00:00: Recorded command exit 0; command argv SHA-256
  9b76d91a2f7b9a47eb310293f9a3cdf6c847128fc95e2aa078071e941daca854.

- 2026-10-09T17:54:47+00:00: Recorded command exit 0; command argv SHA-256
  9758df914fecbac5c2fc27d88d83a599e85bc4133cda88e6e2be630448eeb9a8.

- 2026-10-09T17:54:54+00:00: Recorded command exit 0; command argv SHA-256
  3fd3b384e5d0bb7e8818f3605dbc03a57bfc5129926a7aaf8d17083c505069d1.

- 2026-10-09T17:55:19+00:00: Committed the release vendor and ASB-TUI-owned compatibility updates;
  candidate commit policy, vendor verification, source comparison, headers, doctor, render-status,
  gitleaks, and diff checks pass. Full suite recorded two jsonschema import errors and no behavioral
  failures.

- 2026-10-09T17:55:44+00:00: Recorded command exit 0; command argv SHA-256
  96434223f4e18b45a49e34f98d6474ed6950abea4e2b802b990c7d0c4767136d.

- 2026-10-09T17:55:53+00:00: Recorded command exit 0; command argv SHA-256
  ccb13567c669ae730b3150e3e7f8df535318a84b459298ffd7dfd7d965c8103b.

- 2026-10-09T17:56:45+00:00: Recorded command exit 0; command argv SHA-256
  a1ea4160ba79d0810b99722945a4c1e0adb083cb68c814dd36f4d12c0f0d71be.

- 2026-10-09T17:56:52+00:00: The documented host lacked jsonschema; repository-independent cached uv
  wheels supplied an offline test environment without changing product dependencies. Full suite now
  passes 270 tests; TLC containment remains an expected host capability skip/fail-closed diagnostic.

- 2026-10-09T17:56:58+00:00: Recorded command exit 0; command argv SHA-256
  a533d7bec7cda565c7fc43a7d6d8b3bc3b6e29f2c6a9453f628d4c9df6ed55df.

- 2026-10-09T17:57:11+00:00: Recorded command exit 0; command argv SHA-256
  9b76d91a2f7b9a47eb310293f9a3cdf6c847128fc95e2aa078071e941daca854.

- 2026-10-09T17:57:17+00:00: Recorded command exit 0; command argv SHA-256
  31ac03018d2b73c07530eb891933c9d7a5d785602e81803e4573a407ede8e25a.

- 2026-10-09T17:57:27+00:00: Recorded command exit 0; command argv SHA-256
  9758df914fecbac5c2fc27d88d83a599e85bc4133cda88e6e2be630448eeb9a8.

- 2026-10-09T17:58:18+00:00: Recorded command exit 0; command argv SHA-256
  a1ea4160ba79d0810b99722945a4c1e0adb083cb68c814dd36f4d12c0f0d71be.

- 2026-10-09T17:58:25+00:00: Recorded command exit 0; command argv SHA-256
  a533d7bec7cda565c7fc43a7d6d8b3bc3b6e29f2c6a9453f628d4c9df6ed55df.
