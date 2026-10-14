---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-14T09:59:06+00:00",
  "depends_on": [],
  "id": "AR-1740",
  "next_action": "Verify the exact v0.7.11 release identity and vendor the complete allowlisted snapshot through the official synchronizer in an isolated current-main state worktree.",
  "owner": "asb-tui-state-ar1740-v0711-20261014",
  "plan": "../plans/AR-1740-coordinator-v0711-release-vendor.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1740.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the exact Agent Workflow Coordinator v0.7.11 release and qualify ASB-TUI state compatibility.",
  "task_revision": 17,
  "title": "Coordinator v0.7.11 release vendor for ASB-TUI state",
  "updated_at": "2026-10-14T07:40:31+00:00",
  "worktree_key": ""
}
---

Upgrade the ASB-TUI coordination-state vendor from Coordinator v0.4.0 to the
latest upstream release v0.7.11. The downstream state remains Git-authoritative
and must retain its binding, task history, privacy policy, and all unrelated
work unchanged.

The upstream v0.7.11 lightweight tag resolves to commit
`6f7cb5eeb411898c7812fdebc9da08e1f586c936` and tree
`7a1aa2e956742bb1382a584c9c2f38f1794af815`. Record the lightweight-tag
provenance accurately; do not make an annotated-tag signature claim.


- 2026-10-14T06:59:03+00:00: Upstream v0.7.11 release identity is refreshed and the dedicated
  vendor-upgrade scope is dependency-ready.

- 2026-10-14T06:59:06+00:00: Claimed by asb-tui-state-ar1740-v0711-20261014.

- 2026-10-14T06:59:24+00:00: Recorded command exit 0; command argv SHA-256
  a889c9966cfe28a4891c3a4b0379d0fad9ac2e854ab214adc56b6d5b7fea4e30.

- 2026-10-14T07:00:58+00:00: Recorded command exit 0; command argv SHA-256
  d9cb76d37f968226d2932334ba30eb99fe8623ad97f6cb9ba3ae27638ca3de32.

- 2026-10-14T07:04:58+00:00: Recorded command exit 0; command argv SHA-256
  41700fc9f8374aad22e41615f7b29c2fe044622acb879bd0164a11d18875780f.

- 2026-10-14T07:05:27+00:00: Recorded command exit 0; command argv SHA-256
  18ecd981ba549588728e749e007051942c4343a3029f6827b91e1c8e706aeed2.

- 2026-10-14T07:15:18+00:00: Recorded command exit 0; command argv SHA-256
  1c7c6ef13a2d95f25bd039c2221c9c39bdac7671aa60eb93f0447c6387d7766e.

- 2026-10-14T07:22:56+00:00: Recorded command exit 0; command argv SHA-256
  cd3a4984279c35d860a87b1e575b5fb9c526dbc4ffa6f6106d944b6fcfa5063a.

- 2026-10-14T07:24:18+00:00: Recorded command exit 0; command argv SHA-256
  18ecd981ba549588728e749e007051942c4343a3029f6827b91e1c8e706aeed2.

- 2026-10-14T07:25:06+00:00: Recorded command exit 0; command argv SHA-256
  712d95682383d1ac338f84052f811e4c0ceb7a63812abb94af48129ce7e763d7.

- 2026-10-14T07:25:14+00:00: Recorded command exit 0; command argv SHA-256
  66f8a574910149807057289bdefa24e6287f3b7c786f0f039b6175487bbe275f.

- 2026-10-14T07:28:53+00:00: Recorded command exit 0; command argv SHA-256
  18ecd981ba549588728e749e007051942c4343a3029f6827b91e1c8e706aeed2.

- 2026-10-14T07:34:14+00:00: Recorded command exit 128; command argv SHA-256
  f0f3da6462e32d50a35fe8400efe578645947dfeba3c0704d416c87a2f713589.

- 2026-10-14T07:35:10+00:00: Recorded command exit 0; command argv SHA-256
  b14777b9766e42ea90ceb471a5865c4c7be9abbeaee407c836b03205f0b55735.

- 2026-10-14T07:35:15+00:00: Recorded command exit 0; command argv SHA-256
  bd4c1f78097a36de03ca6e2ebf91427a3ffa77fbc8102a9fd5cb13b9614cd065.

- 2026-10-14T07:40:31+00:00: Recorded command exit 0; command argv SHA-256
  84d7755805e55a82b7d288dbf7d1103cb40c32876d017cb39d69b58c611eebd7.
