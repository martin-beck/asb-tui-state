---
{
  "branch": "feature/ar-1324-install-and-broker-onboarding",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T08:05:48+00:00",
  "depends_on": [
    "AR-1200"
  ],
  "id": "AR-1324",
  "next_action": "Promote after AR-1200; implement the clean development install, broker negotiation, and recovery route with explicit fixture/warning labels.",
  "owner": "tui-ar1324-dev-20261001",
  "plan": "../plans/AR-1324.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make clean development ASB/asb-tui installation and local broker onboarding a selectable first step.",
  "task_revision": 9,
  "title": "Install and broker onboarding",
  "updated_at": "2026-09-30T06:10:24+00:00",
  "worktree_key": "asb-tui-ar-1324-install-and-broker-onboarding"
}
---

The TUI must not become a second installer or protocol authority; it renders
the verified ASB installation/control contract.

- 2026-09-30T06:01:58+00:00: Development-only gate policy now removes paired ASB/production
  prerequisites. AR-1200 is complete at 406a6da; promote clean development install and broker
  onboarding against local fixtures.

- 2026-09-30T06:02:01+00:00: Claimed by tui-ar1324-dev-20261001.

- 2026-09-30T06:02:14+00:00: Recorded command exit 0; command argv SHA-256
  d6da7c2716462328d785ed41a39c1c5223f9c2bc1dafe79542ecf2283b871336.

- 2026-09-30T06:05:14+00:00: Recorded command exit 0; command argv SHA-256
  83b5913d0f9bffc6ad2f27e8d01ef0c0f4d481b24ffac654e648fa1423bb460a.

- 2026-09-30T06:05:30+00:00: Recorded command exit 0; command argv SHA-256
  979f297d9371bf1b847107ec75341425c3163094a34fd201bb1a7e4017f0d849.

- 2026-09-30T06:05:48+00:00: Heartbeat by tui-ar1324-dev-20261001.

- 2026-09-30T06:07:22+00:00: Recorded command exit 0; command argv SHA-256
  3fbf0341eb1a475273d1bbb23ff2a1d0b530fbcb22f7cefce41bce121f5ddb97.

- 2026-09-30T06:10:24+00:00: Recorded command exit 0; command argv SHA-256
  588ce13b80170c5ef5f49e6dc8614e84c3533d433772e70b31c3f711817c7552.
