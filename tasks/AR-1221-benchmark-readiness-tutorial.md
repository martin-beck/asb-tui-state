---
{
  "branch": "docs/ar-1221-tui-readiness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T13:26:25+00:00",
  "depends_on": [
    "AR-1220"
  ],
  "id": "AR-1221",
  "next_action": "Implement the syntax-checked TUI tutorial for testing current agent benchmark readiness.",
  "observed_branch": "docs/ar-1221-tui-readiness",
  "observed_dirty": 0,
  "observed_head": "11f4a0671da40a67ee3143dd5bec149390a6aa74",
  "owner": "codex-asb-tui-ar1221-readiness-20260916",
  "plan": "../plans/AR-1221.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Teach users to inspect TUI benchmark readiness without performing a run.",
  "task_revision": 24,
  "title": "asb-tui benchmark-readiness tutorial",
  "updated_at": "2026-09-16T12:26:40+00:00",
  "worktree_key": "asb-tui-ar-1221"
}
---

Implement the linked tutorial and deterministic offline state fixtures only.

- 2026-09-16T12:12:56+00:00: AR-1220 is merged at d6acbc7 and ASB tutorial contract v1 is published;
  benchmark-readiness tutorial can proceed with synthetic offline fixtures.

- 2026-09-16T12:13:10+00:00: Claimed by codex-asb-tui-ar1221-readiness-20260916.

- 2026-09-16T12:15:15+00:00: Heartbeat by codex-asb-tui-ar1221-readiness-20260916.

- 2026-09-16T12:15:33+00:00: Heartbeat by codex-asb-tui-ar1221-readiness-20260916.

- 2026-09-16T12:15:49+00:00: Recorded command exit 0; command argv SHA-256
  dee9698896ce66137446179d6254e7bb595f2e40295247fca2ef929a18415765.

- 2026-09-16T12:16:12+00:00: Recorded command exit 0; command argv SHA-256
  b8bbf38d076c974821d1cbf8ac8f9b52eaf3ba9207d9e0cf1a80c01c371c207f.

- 2026-09-16T12:17:34+00:00: Recorded command exit 128; command argv SHA-256
  204671a3efa50fef0c274a878ae51d04f0b07cf58ce70de3b602157d49830901.

- 2026-09-16T12:17:49+00:00: Recorded command exit 0; command argv SHA-256
  b87ffbac85c5f8806c5975009f46c9c0b3fd162effcaeff0fc82091aca42ddf7.

- 2026-09-16T12:18:31+00:00: Recorded command exit 0; command argv SHA-256
  e9db36821af1d523dbe38f7f6a2c3862811e376e94a952c580f1cda2b121a98c.

- 2026-09-16T12:19:23+00:00: Recorded command exit 0; command argv SHA-256
  377e144c6e0a61cac3c896e7df5cb46633ce660a8f3aedca7d48345784e0d572.

- 2026-09-16T12:19:37+00:00: Recorded command exit 0; command argv SHA-256
  a9eb35ffb2d3abfb63c21081aa37f776cb801355cd9a82a755e8951d814079b6.

- 2026-09-16T12:19:58+00:00: Heartbeat by codex-asb-tui-ar1221-readiness-20260916.

- 2026-09-16T12:20:34+00:00: Recorded command exit 0; command argv SHA-256
  2ad9c51ef8c0130716779c65806db6be888a298525e6a36229afe30729d4e61a.

- 2026-09-16T12:20:50+00:00: Heartbeat by codex-asb-tui-ar1221-readiness-20260916.

- 2026-09-16T12:21:11+00:00: Implementation complete and published as PR #108 at exact head
  f4fe1349fff65a7c133d82f64bc1bb9c372c0239, based on origin/main d6acbc7. Added
  docs/tutorials/benchmark-readiness-v1.json and benchmark-readiness.md; four synthetic offline
  state fixtures covering ready, incomplete, unavailable, and platform-incompatible; and
  tools/test-benchmark-readiness-tutorial.py with strict navigation/action ordering, refusal,
  redacted credential, shell/path/secret, and closed-fixture checks. Added validator to
  .github/workflows/quality.yml. Evidence: python3 tools/test-benchmark-readiness-tutorial.py
  passed; cargo fmt --all --check passed; cargo test --locked passed (136 unit, 1 binary, and full
  integration suite); existing tutorial/help/state validators passed. No ASB, agent, provider, LLM,
  benchmark, or network execution. Next: coordinator review/merge PR #108 after exact-head CI is
  green.

- 2026-09-16T12:26:25+00:00: Claimed by codex-asb-tui-ar1221-readiness-20260916.

- 2026-09-16T12:26:34+00:00: Recorded command exit 0; command argv SHA-256
  438a609eba65643767416c25b32a407d58148de7877ca5f380fbdc042fd8fe10.
