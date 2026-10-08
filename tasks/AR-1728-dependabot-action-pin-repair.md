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
  "owner": "codex-tui-ar1728-action-pin-20261009",
  "plan": "../plans/AR-1728-dependabot-action-pin-repair.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1728.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Integrate the taiki-e/install-action pin update carried by stale DCO-invalid Dependabot PR #288 without weakening signature, DCO, exact-main, or independent-review requirements.",
  "task_revision": 3,
  "title": "Rebuild Dependabot action-pin update on current main",
  "updated_at": "2026-10-08T23:11:02+00:00",
  "worktree_key": "asb-tui-ar1728-install-action-pin"
}
---

Dependabot PR #288 changes only `.github/workflows/trusted-main.yml`, updating
`taiki-e/install-action` from immutable commit
`76b5a2d6647bc0a6b597e5640070b9dc07966d4c` to immutable commit
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
