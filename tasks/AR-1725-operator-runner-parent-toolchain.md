---
{
  "branch": "repair/ar-1725-operator-runner-parent-toolchain",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T16:47:28+00:00",
  "depends_on": [
    "AR-1721",
    "AR-1724"
  ],
  "id": "AR-1725",
  "next_action": "Repair tools/run-operator-quickstart.py so it resolves and forwards the validated parent ASB Cargo/Rustup inputs before replacing HOME, add real isolated-HOME and hostile-input regressions, rerun the exact paired public journey, obtain independent review, merge, and verify exact-main CI.",
  "observed_branch": "repair/ar-1725-operator-runner-parent-toolchain",
  "observed_dirty": 0,
  "observed_head": "db6839c86e73f3e3c10e8c0b336fbc5a1329b443",
  "owner": "codex-tui-ar1725-parent-toolchain",
  "plan": "../plans/AR-1725-operator-runner-parent-toolchain.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "sha256:edabf732aab0b25d9b3378332c263a040fb98c497115af1319d54a567bed81d9",
    "evidence_ref": "quality/AR-1725-operator-runner-parent-toolchain-20261008.json",
    "spec_ref": "specs/AR-1725.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1725.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Keep the public operator quickstart usable under its isolated HOME by propagating the validated parent ASB development toolchain boundary.",
  "task_revision": 31,
  "title": "Operator quickstart parent toolchain propagation repair",
  "updated_at": "2026-10-08T13:39:03+00:00",
  "worktree_key": "asb-tui-ar-1725-operator-runner-parent-toolchain"
}
---

AR-1575 final qualification at ASB
`fd956d857970f039db0a4aad03c9e15e59b13da6` and asb-tui
`50acbc4af69480b7fbd34db19520a96ce1190a67` proved that normal ASB source
materialization, status, doctor, upgrade, removal, and the paired
credential-free journey work after ASB AR-1737 and TUI AR-1654.

The documented `tools/run-operator-quickstart.py` gate still replaces `HOME`
with a disposable root before invoking the parent `asb` binary. It forwards
only the child-facing `ASB_TUI_DEV_RUSTUP_HOME` value. The parent router
resolves `ASB_DEV_CARGO` and `ASB_DEV_RUSTUP_HOME`, so bare `asb tui` fails
before executing the installed TUI with typed `trusted_tool_unavailable`.
The identical exact-head gate passes completely when those two validated
parent inputs are supplied: bare launch returns `development_launched` through
the real 80x24 controlling foreground PTY, and all four wizard, setup,
benchmark, recording/replay, and comparison suites pass. The privacy-safe
control receipt has SHA-256
`48903d51c51a418ec910dea9f09e348febd460802285bbb5952fc8c20b84faef`.

Repair only asb-tui qualification tooling and its tests. Resolve the original
host toolchain boundary before installing the disposable `HOME`, then pass
the bounded values through the parent ASB names while retaining the existing
child-facing TUI handoff. ASB remains responsible for validating ownership,
permissions, symlinks, selected-toolchain consistency, descriptor binding,
and substitution resistance. Do not hard-code a host path, inherit secrets,
weaken hostile-layout failures, add provider access, or change ASB, renderer,
wizard, or runtime behavior. Development authentication, signatures, key
management, and provider credentials remain warning-only and never block this
gate.


- 2026-10-08T12:47:28+00:00: Claimed by codex-tui-ar1725-parent-toolchain.

- 2026-10-08T12:51:49+00:00: Recorded command exit 0; command argv SHA-256
  c88f2c5cde1143c5e65215dcce942641c448a54ef05329764ed7a6c5137e463e.

- 2026-10-08T12:55:40+00:00: Recorded command exit 0; command argv SHA-256
  b748788cb32d5d76b8c77ddde9b3c443c4455947f5471db14cf9e8221f33b4d5.

- 2026-10-08T12:57:00+00:00: Recorded command exit 0; command argv SHA-256
  b748788cb32d5d76b8c77ddde9b3c443c4455947f5471db14cf9e8221f33b4d5.

- 2026-10-08T13:05:51+00:00: Recorded command exit 0; command argv SHA-256
  49d3c64612ebfb375cd964964a542c1f9fe6abf41f7a75059abb66b47e1e3a18.

- 2026-10-08T13:09:30+00:00: Recorded command exit 0; command argv SHA-256
  60ef893e5e99b6de3c67194553e211eca8b22884d77718beeaf77a6861cf77ca.

- 2026-10-08T13:10:56+00:00: Recorded command exit 0; command argv SHA-256
  483c325407f5685d854771893641aa67e366169b8d0a1752b1c42aa9cc374047.

- 2026-10-08T13:11:45+00:00: Recorded command exit 0; command argv SHA-256
  d8288ccf6bcc2417d5a3fa2f4a36babe4478464e54b8fd4ebc8caf623d8358ed.

- 2026-10-08T13:12:40+00:00: Recorded command exit 0; command argv SHA-256
  60ef893e5e99b6de3c67194553e211eca8b22884d77718beeaf77a6861cf77ca.

- 2026-10-08T13:16:07+00:00: Recorded command exit 0; command argv SHA-256
  e4283adf993357c75c91d1c049d0c6be049b083f3899df504b4524cf61f86bf9.

- 2026-10-08T13:16:28+00:00: Recorded command exit 0; command argv SHA-256
  d0b782e0aae735e6d1e6db71ccd2f29b967c5f935fd03193d975bd5a18b0f724.

- 2026-10-08T13:17:09+00:00: Recorded command exit 0; command argv SHA-256
  4d4e2e84ef7765f6be490e597dc5c1153a47d8de81897276fe4b843bc87338f2.

- 2026-10-08T13:17:28+00:00: Recorded command exit 1; command argv SHA-256
  b234e05c52045be44ef6e14763298e37c9926ed9cc7817a6bb7630efe52e746d.

- 2026-10-08T13:18:37+00:00: Recorded command exit 0; command argv SHA-256
  60ef893e5e99b6de3c67194553e211eca8b22884d77718beeaf77a6861cf77ca.

- 2026-10-08T13:19:30+00:00: Recorded command exit 0; command argv SHA-256
  60ef893e5e99b6de3c67194553e211eca8b22884d77718beeaf77a6861cf77ca.

- 2026-10-08T13:19:44+00:00: Recorded command exit 0; command argv SHA-256
  1ab006b9babd2307add8e476b9d7c96ac75e7053400483360882612abce99bdb.

- 2026-10-08T13:20:29+00:00: Recorded command exit 0; command argv SHA-256
  a028c5678d12dc15dd17f4c17089ac618f6aa4e71706361d42da1a3b86a804f2.

- 2026-10-08T13:21:30+00:00: Recorded command exit 0; command argv SHA-256
  78ddd60b33b9f0da334f7379e7bbff5fa2b2dc92b00f045a327d10909d4284ef.

- 2026-10-08T13:21:55+00:00: Recorded command exit 0; command argv SHA-256
  69b410aa8221bbb41fc20fd06ab228a1ca781324b88dc3177a4be4ba7272f3dd.

- 2026-10-08T13:22:23+00:00: Recorded command exit 0; command argv SHA-256
  c86900dd188b5353cd167c06e0a2e6a9ed7fd295afdd58214d908b9ba953fb12.

- 2026-10-08T13:23:01+00:00: PR #294 publishes signed+DCO commit
  db6839c86e73f3e3c10e8c0b336fbc5a1329b443 tree b57c21fdf90404cc8a743e389ea1e2cd8528cfa7. Full local
  gates and 46 focused tests passed. Exact paired no-override candidate journey passed with TUI
  executable SHA-256 7f7743aa660e3f1fa370408b648d1f9998c5569a8df6759efd787fe218c2a74f and
  privacy-safe receipt SHA-256 90cddd1d11fc16b30809fd02140de792ff315572dcdb4bea469f9de83edde871.
  Await independent final review and terminal green PR checks before coordinator merge.

- 2026-10-08T13:29:37+00:00: Recorded command exit 0; command argv SHA-256
  a70d234d7eaacc221a4dd111ce1692425678e41f6d6cc7228e2f30b3efca0b52.

- 2026-10-08T13:30:01+00:00: Recorded command exit 0; command argv SHA-256
  0ab306b50348075be6bddc13bcd37f4c2927bc3d674239dc285db3d584644158.

- 2026-10-08T13:38:05+00:00: Recorded command exit 0; command argv SHA-256
  295a36ead997dee194faa41e3c5a6df62f0e241de14a0ba6125245bca6fba22b.

- 2026-10-08T13:39:03+00:00: Recorded pass acceptance for complete specs/AR-1725.json revision 1
  against privacy-safe exact-merge receipt
  quality/AR-1725-operator-runner-parent-toolchain-20261008.json SHA-256
  edabf732aab0b25d9b3378332c263a040fb98c497115af1319d54a567bed81d9.
