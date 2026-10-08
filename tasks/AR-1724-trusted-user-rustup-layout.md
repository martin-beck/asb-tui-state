---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T12:37:58+00:00",
  "depends_on": [
    "AR-1714",
    "AR-1723"
  ],
  "id": "AR-1724",
  "next_action": "Promote and repair TUI development Cargo discovery for the conventional owner-owned Rustup layout, then rerun the detached exact-main fresh-user journey.",
  "owner": "codex-ar1724-rustup-layout-20261008",
  "plan": "../plans/AR-1724-trusted-user-rustup-layout.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Accept the conventional owner-owned group-writable Rustup development layout with an explicit warning while keeping executable and substitution boundaries fail-closed.",
  "task_revision": 19,
  "title": "Trusted owner Rustup layout and detached quickstart repair",
  "updated_at": "2026-10-08T08:46:12+00:00",
  "worktree_key": ""
}
---

AR-1597 exact-main requalification showed that the standalone TUI returns
`development_tool_unavailable` for the current host conventional Rustup shim:
the shim and resolved toolchain executables are regular, owner-controlled and
non-writable by group/other, while owner-controlled Rustup directories and
`settings.toml` use the common group-writable development layout. Current ASB
already accepts this narrow layout with a visible development warning.

Repair only the standalone `asb-tui` implementation and qualification tools.
Development authentication, signatures, and key management remain visible
warnings and never block local/mock execution. Do not modify ASB product code.


- 2026-10-08T08:37:55+00:00: Dependencies AR-1714 and AR-1723 are done. AR-1597 exact-main
  reproduction proves the conventional owner-owned Rustup layout and detached-wrapper gaps;
  implement the narrow TUI-only repair with hostile-path rejection.

- 2026-10-08T08:37:58+00:00: Claimed by codex-ar1724-rustup-layout-20261008.

- 2026-10-08T08:38:14+00:00: Recorded command exit 0; command argv SHA-256
  ebb630ca5026e9d1b388242e978e236f440f70b35548843e8a081a9f7f738a81.

- 2026-10-08T08:38:32+00:00: Recorded command exit 0; command argv SHA-256
  fa38fddc44bfcc1230a8ebafa4fdd340651525b4b50c3e6e15e2d8541b1ffa81.

- 2026-10-08T08:38:52+00:00: Recorded command exit 0; command argv SHA-256
  b5e8c5b81a87760c70c2b7a855f6b119e2fe76e5b964c0c87d2d0907788278fb.

- 2026-10-08T08:39:10+00:00: Recorded command exit 0; command argv SHA-256
  a1d18de80fa5f703b1d0f88ead586ab6f97630e1a8ab58551d2697cf9dbb1c0c.

- 2026-10-08T08:39:29+00:00: Recorded command exit 0; command argv SHA-256
  86a182dbe7edd09136403ebe8b230e7332decb669891fee5a788ce9f0a8ac1a0.

- 2026-10-08T08:39:53+00:00: Recorded command exit 0; command argv SHA-256
  7461789e9f5d1b6824bc7cdcc4ff4e00749879e258475d5d6cb941b183ab6bec.

- 2026-10-08T08:40:20+00:00: Recorded command exit 0; command argv SHA-256
  e2ec55bcdea0e985546f5e32b7d2b24f65de417704cd5d1575e8d2c5398a6ff2.

- 2026-10-08T08:40:40+00:00: Recorded command exit 0; command argv SHA-256
  bfe30f89e0542c5243af2c577106ddfe00ae2a5ed6ced11b41cd24ffea6cbde2.

- 2026-10-08T08:42:23+00:00: Recorded command exit 101; command argv SHA-256
  63966ca07ebaf85f77014d0f83c2ab4e3037f079c7fe5f3b8373877450d415cb.

- 2026-10-08T08:42:50+00:00: Recorded command exit 0; command argv SHA-256
  29a6a451f7e6928b3dbff1bd393cd198484cf7a19e56a3db75f26b725f0b2eaa.

- 2026-10-08T08:43:52+00:00: Recorded command exit 0; command argv SHA-256
  38e4690de1f70789fdae5a0b65a0bad1118548f5f015f2369cda9f5eefc74c9a.

- 2026-10-08T08:44:17+00:00: Recorded command exit 101; command argv SHA-256
  59197a9b96e3cf5c5e5efb4efcfd9e5d609c3bd0a12ca7d7696905c854830cc4.

- 2026-10-08T08:44:42+00:00: Recorded command exit 0; command argv SHA-256
  0cf1d5a99643768ac695a477b5e55deb1fe50d910051006797baeee962127bd0.

- 2026-10-08T08:45:14+00:00: Recorded command exit 101; command argv SHA-256
  59197a9b96e3cf5c5e5efb4efcfd9e5d609c3bd0a12ca7d7696905c854830cc4.

- 2026-10-08T08:45:38+00:00: Recorded command exit 0; command argv SHA-256
  5aa618a5ddc4f2bb88a23a91dbcff6274a6679f52d5a8d8a209595c235a72718.

- 2026-10-08T08:46:12+00:00: Recorded command exit 0; command argv SHA-256
  72078c00e32013db11dd2260bec9df4023e631fbcec73afa011079568529015e.
