---
{
  "branch": "repair/ar-1728-install-action-pin",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T01:10:43+00:00",
  "depends_on": [
    "AR-1725"
  ],
  "id": "AR-1728",
  "next_action": "Reproduce Dependabot PR #288's reviewed one-line immutable action-pin update from exact current main with project-compliant SSH signature and matching DCO, then independently review, merge, verify exact-main CI, and close the superseded Dependabot PR.",
  "observed_branch": "repair/ar-1728-install-action-pin",
  "observed_dirty": 0,
  "observed_head": "4a7fda9eda8b6f2a792972ed962892f3ac8a88eb",
  "owner": "codex-tui-ar1728-action-pin-20261009",
  "plan": "../plans/AR-1728-dependabot-action-pin-repair.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1728.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Integrate the taiki-e/install-action pin update carried by stale DCO-invalid Dependabot PR #288 without weakening signature, DCO, exact-main, or independent-review requirements.",
  "task_revision": 25,
  "title": "Rebuild Dependabot action-pin update on current main",
  "updated_at": "2026-10-08T23:25:49+00:00",
  "worktree_key": "asb-tui-ar1728-install-action-pin"
}
---

Dependabot PR #288 changes only `.github/workflows/trusted-main.yml`, updating
`taiki-e/install-action` from immutable commit
`4076c08d76dba979c11a7285295b0716c1d67908` to immutable commit
`83ac0ad63c0167e6f06796fab0fce28db1bf3db0`. Independent read-only review found
no defect in that dependency delta, but the PR is based on
`69f0584cee27001b1ae10b7311192124a855858c`, trails current main, has no
independent GitHub approval, and fails both required workflows because its
author and `Signed-off-by` emails differ. Its GitHub GPG verification is not the
project-required SSH-signed candidate evidence.

Rebuild exactly that one-line pin change from current remote main in this AR's
isolated worktree. Do not merge, rebase, amend, or force-push the Dependabot
branch. Verify the target commit exists in the upstream action repository and
review the bounded upstream diff between the old and new pins for changes to
the action entrypoints used by `trusted-main.yml`. Run YAML/action pinning,
privacy, supply-chain, repository quality, and applicable full project gates.

Publish one SSH-signed commit with a matching DCO trailer, obtain independent
exact-head/tree review, merge only the reviewed tree through the protected
signed workflow, and require both exact-main Repository Quality and Trusted
Main runs to succeed. Close PR #288 as superseded only after the replacement
merge and post-merge verification are durable. Development release/auth policy
remains warning-only; dependency identity, signature, DCO, review, CI, and
post-merge validation are mandatory.

- 2026-10-08T23:10:43+00:00: Claimed by codex-tui-ar1728-action-pin-20261009.

- 2026-10-08T23:11:02+00:00: Recorded command exit 0; command argv SHA-256
  f43ee155069b462694bf579d2cf5e463beeae0b4462c4a8d0e3af02ce49b636c.

- 2026-10-08T23:11:16+00:00: Recorded command exit 0; command argv SHA-256
  2ee645c02420331501bf6f49c31a8c7e5398d036d918e3d78814446913a7c836.

- 2026-10-08T23:12:06+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-08T23:12:30+00:00: Recorded command exit 0; command argv SHA-256
  bbc07e543e53f68406e5e3fc42762cb295c6f1f7e41d8d987408075cd27f1c7b.

- 2026-10-08T23:13:12+00:00: Recorded command exit 0; command argv SHA-256
  9c3b938fca33fe1fdc4495685e6a1e7dd1b373f2b4d685fcfbef4e1fa5bcea61.

- 2026-10-08T23:14:51+00:00: Recorded command exit 0; command argv SHA-256
  7c0758348a69ce85a12fb6e9db133c56d1b94f2815c6817884711062aece1956.

- 2026-10-08T23:15:09+00:00: Recorded command exit 0; command argv SHA-256
  a1b701c2196168e96a79cc425e5b1d71e594bd11a87b19fe2cfd2f2993158fd5.

- 2026-10-08T23:15:53+00:00: Recorded command exit 101; command argv SHA-256
  b7bc3cb6cf121191ccca0750bb2fede133623c3c00fd2e5a96cc5a288b7b9305.

- 2026-10-08T23:16:41+00:00: Recorded command exit 0; command argv SHA-256
  a0b92928022a42c23c7b426c2f7203af94e9650389be678e976f75ecac9af91e.

- 2026-10-08T23:18:54+00:00: Recorded command exit 0; command argv SHA-256
  67b557f4fba4e642381f7e151aaa5c01658e0e77f010d40aeb97d049c4c112d5.

- 2026-10-08T23:19:10+00:00: Recorded command exit 1; command argv SHA-256
  48dbf3d5290e547148ce9e9c93d30b464e573f24c4a3e11719f0b8b5095bfee7.

- 2026-10-08T23:19:27+00:00: Recorded command exit 0; command argv SHA-256
  aef9ec90cf4e22cb8b0ff2b92f8260033356aae23f30ac958960f6c7bf95c6e8.

- 2026-10-08T23:20:43+00:00: Recorded command exit 0; command argv SHA-256
  6d151b699e075aa8645fcd8c00fcb6efd15330b52a617e2676dc9d6ed02582d9.

- 2026-10-08T23:21:19+00:00: Recorded command exit 0; command argv SHA-256
  0be096fb59b8ccb0052fbdbf3099822bdf16116dba2ced7d23aa77fdb70dfb5b.

- 2026-10-08T23:22:21+00:00: Recorded command exit 0; command argv SHA-256
  361200a125fda2a512db9fa96f6fc2b9e9852bb9b7a3221b61093180e9141866.

- 2026-10-08T23:22:39+00:00: Recorded command exit 0; command argv SHA-256
  8f867e7aedddd3440fea6077777705b1ce1cecb953f3179a4d4131d0ec5e610f.

- 2026-10-08T23:24:50+00:00: Recorded command exit 0; command argv SHA-256
  8d1a5c18c514c9821f0eb5889c8c905209c87cbb2b045ae7f091922d9909bcb4.

- 2026-10-08T23:25:13+00:00: Recorded command exit 0; command argv SHA-256
  4a4b8b17fbfcb29543b2f2c744a6f1a89f3d5ff7a0ff6df9f965dc94baf2e797.

- 2026-10-08T23:25:31+00:00: Recorded command exit 0; command argv SHA-256
  88c13f83430be5a9c2f60a1d94fe6e37bc033f6eaa7e4b634ebb6da16bf3717a.

- 2026-10-08T23:25:49+00:00: Recorded command exit 0; command argv SHA-256
  58d59edeb0306b78b28c7fbe398ecf04fb056a6aa4520ac9e98a61174b5cb959.
