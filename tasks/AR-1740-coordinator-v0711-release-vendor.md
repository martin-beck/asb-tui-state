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
  "retry_circuit": {
    "abandoned": [],
    "attempts": [],
    "hold": null,
    "recoveries": [],
    "reservations": [
      {
        "expires_at": "2026-10-14T08:28:20+00:00",
        "id": "9b45575f53fc41139703eb2d157b6b75",
        "identity": "sha256:807588f22c8d4fa05b4720fcecafacc2d14733d2581962706735fa999847ac35",
        "progress_digest": "sha256:5fac4bda38e4a3df8ea06a1946c455591cbd5abd0c255c7168c133926aca5bbe",
        "reserved_at": "2026-10-14T07:57:20+00:00",
        "task_revision": 27,
        "window": 3
      }
    ],
    "schema_version": 1
  },
  "schema_version": 1,
  "spec_ref": "specs/AR-1740.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the exact Agent Workflow Coordinator v0.7.11 release and qualify ASB-TUI state compatibility.",
  "task_revision": 28,
  "title": "Coordinator v0.7.11 release vendor for ASB-TUI state",
  "updated_at": "2026-10-14T07:57:20+00:00",
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

- 2026-10-14T07:40:36+00:00: Recorded command exit 0; command argv SHA-256
  36ae015551cabfc9ab5b1dfe5cbae8be69f140053a1795287127de73c6a0c1c8.

- 2026-10-14T07:44:10+00:00: Recorded command exit 0; command argv SHA-256
  2bf7d1978f71bfb8ae407346ba295cbe39ceb9a299a0c36918515adfd47f0212.

- 2026-10-14T07:45:13+00:00: Recorded command exit 0; command argv SHA-256
  c562eb0aa360c056f636a9d704e4c1364fd6eba9579cd61617f93cd9cbacd00d.

- 2026-10-14T07:51:36+00:00: Recorded command exit 0; command argv SHA-256
  ee0b4be8ec6068a496af99e00b4d58a4a90f794707737068efcf2191de7e9b95.

- 2026-10-14T07:53:49+00:00: Reserved retry circuit launch slot; expired_slots_cleaned=0.

- 2026-10-14T07:53:53+00:00: Released retry circuit launch slot.

- 2026-10-14T07:53:56+00:00: Recorded command exit 0; command argv SHA-256
  be30c52d74ba52c5b0ea3e2267475c09f97dcbd072da29a36a21cf5377c29d6b.

- 2026-10-14T07:57:10+00:00: Reserved retry circuit launch slot; expired_slots_cleaned=0.

- 2026-10-14T07:57:13+00:00: Released retry circuit launch slot.

- 2026-10-14T07:57:15+00:00: Recorded command exit 0; command argv SHA-256
  763a123a24e6002a08eb9cfeff35c852ded9d851a58428ef0cb59e3c0f226939.

- 2026-10-14T07:57:20+00:00: Reserved retry circuit launch slot; expired_slots_cleaned=0.
