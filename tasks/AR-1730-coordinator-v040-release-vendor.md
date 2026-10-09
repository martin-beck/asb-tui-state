---
{
  "branch": "upgrade/ar-1730-coordinator-v0.4.0-release",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T20:46:52+00:00",
  "depends_on": [],
  "id": "AR-1730",
  "next_action": "Vendor sync and exact 79-file source/tree/mode/digest comparison pass in isolated worktree. Prepare signed DCO candidate after reviewing full vendor diff; rerun full tests with host jsonschema dependency or record that environmental blocker, then independent review.",
  "owner": "codex-asb-tui-ar1730-v040-20261009",
  "plan": "../plans/AR-1730-coordinator-v040-release-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1730.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the exact Agent Workflow Coordinator v0.4.0 release and qualify ASB-TUI state compatibility without patching vendored bytes or weakening provenance gates.",
  "task_revision": 23,
  "title": "Coordinator v0.4.0 release vendor for ASB-TUI compatibility",
  "updated_at": "2026-10-09T17:53:18+00:00",
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
