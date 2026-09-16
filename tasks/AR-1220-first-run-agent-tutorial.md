---
{
  "branch": "docs/ar-1220-first-run-agent",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T14:09:47+00:00",
  "depends_on": [],
  "id": "AR-1220",
  "next_action": "Coordinator to monitor PR #107 exact head fb9d4b86270f4be11102868caff226fe35900e78, obtain independent review, and merge only after all required checks pass; then perform post-merge assurance.",
  "observed_branch": "docs/ar-1220-first-run-agent",
  "observed_dirty": 0,
  "observed_head": "adf1270df6bb39a0321b5eac5d5f38ce36eccf01",
  "owner": "codex-asb-tui-ar1220-dco-fix-20260916",
  "plan": "../plans/AR-1220.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Teach first-time users to initialize asb-tui and configure their first agent connection.",
  "task_revision": 22,
  "title": "asb-tui first-run and first-agent tutorial",
  "updated_at": "2026-09-16T12:09:55+00:00",
  "worktree_key": "asb-tui-ar-1220"
}
---

Implement the linked tutorial and offline route/state fixtures. Cross-repository dependency on ASB
AR-1210 is recorded in the plan; do not run tutorial actions or connect to an agent in CI.

- 2026-09-16T11:59:22+00:00: ASB tutorial contract is now published by merged ASB PR #184 at
  4d4a0c4f3bd71f9884c9cc06649ba6722fa03bff. AR-1220 remains synthetic/offline and does not require
  live ASB catalog/lifecycle execution.

- 2026-09-16T11:59:36+00:00: Claimed by codex-asb-tui-ar1220-tutorial-20260916.

- 2026-09-16T12:00:14+00:00: Recorded command exit 0; command argv SHA-256
  0b3144e96c4613382328544894c86d35db9e80c40da13c499d63bec6d4c9c3e7.

- 2026-09-16T12:02:38+00:00: Heartbeat by codex-asb-tui-ar1220-tutorial-20260916.

- 2026-09-16T12:05:04+00:00: Recorded command exit 0; command argv SHA-256
  e006d26233efe97c8613057a8fdd3a246dcd807f98c9d74430d419abef18be2e.

- 2026-09-16T12:05:25+00:00: Recorded command exit 1; command argv SHA-256
  6606c1b4e43aed61ccb1333d4b573d09cb4e7b36372002f01cfb7e6de7c5d775.

- 2026-09-16T12:05:44+00:00: Recorded command exit 0; command argv SHA-256
  48e3c4e24afdd26a7e068a54db983f6796b1c1f17478713b4f7dd2af99484fba.

- 2026-09-16T12:06:05+00:00: Recorded command exit 0; command argv SHA-256
  cb72620942961cf546cce778d1e87d28eec7546d7de2ccf0189547b177957827.

- 2026-09-16T12:06:18+00:00: Recorded command exit 1; command argv SHA-256
  096de54e36da83f56c7da48530b2d812b951d00b4a33842a1434ce0e6836bdd6.

- 2026-09-16T12:06:39+00:00: Recorded command exit 0; command argv SHA-256
  3fab0e8e2aed276c54d218707cd89bab5cf35df696a098f763647cdeb7bbd9f0.

- 2026-09-16T12:06:47+00:00: Recorded command exit 1; command argv SHA-256
  972c971991d4bc0a3ae1f3dab4c7b869f277ada19ca3201bdf42253af075509e.

- 2026-09-16T12:06:54+00:00: Recorded command exit 0; command argv SHA-256
  4fd5fbf65a9a624088ebf4c889c8bc5160c808ce8c7c18978d2f70ef2fa5b979.

- 2026-09-16T12:07:12+00:00: Recorded command exit 0; command argv SHA-256
  14c8b278fb9fbdbf513c5ad8b88abecc382642e01cd6be71d2cb829a7f384ce2.

- 2026-09-16T12:07:38+00:00: Implementation complete and published without merge. Product branch
  docs/ar-1220-first-run-agent exact head fb9d4b86270f4be11102868caff226fe35900e78 adds the
  machine-readable first-run/first-agent tutorial, human journey documentation, and deterministic
  offline validator with negative network/option-order cases; CI invokes the validator. It uses
  synthetic identities/digests only and never runs ASB, providers, agents, benchmarks, or tutorial
  commands. Exact-head local evidence: validator, JSON parse, fmt, cargo test --locked (136 library
  tests plus all integration suites), clippy, UI help/model, compatibility, release/publication,
  shell quality, actionlint/zizmor, and Gitleaks completed; the broad private-material grep produced
  one pre-existing false positive in tools/validate-ui-help.py and was not changed. Commit is
  SSH-signed and DCO-compliant. PR #107 is open, non-draft, mergeable; hosted Repository quality is
  in progress and AWQ prerequisite is queued.

- 2026-09-16T12:07:45+00:00: Implementation handoff released for coordinator review. PR #107 remains
  unmerged; monitor exact-head hosted checks and obtain independent review before merge.

- 2026-09-16T12:09:47+00:00: Claimed by codex-asb-tui-ar1220-dco-fix-20260916.

- 2026-09-16T12:09:49+00:00: Recorded command exit 0; command argv SHA-256
  45758df213987ae0a1501f8779b9c70f039029f29fe089f3a1853f25b868915d.
