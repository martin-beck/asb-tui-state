---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1673",
    "AR-1722"
  ],
  "id": "AR-1726",
  "next_action": "Replace the lifecycle-brittle AR-1673 profile assertion with phase-complete invariant checks, run the full state and formal gates, obtain independent review, and restore exact-main Coordination verification to green.",
  "owner": "",
  "plan": "../plans/AR-1726-supersession-profile-lifecycle.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1726.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Make the supersession profile gate valid across AR-1673's dependency-ready, actively claimed, and accepted terminal lifecycle without weakening ownership or acceptance invariants.",
  "task_revision": 1,
  "title": "Repair supersession profile lifecycle gate",
  "updated_at": "2026-10-08T14:00:00+00:00",
  "worktree_key": ""
}
---

## Problem statement

AR-1722 added a downstream profile test proving that superseded AR-1672 is
satisfied by completed replacement AR-1668 and therefore admits AR-1673. The
test coupled that invariant to AR-1673's instantaneous status. It first
required exactly `open`, then a partial repair admitted `open` and a valid
`in_progress` claim but omitted the required terminal `done` state. As a
result, valid handoffctl transitions caused hosted Coordination verification
to fail both when AR-1673 was claimed and after it was released done.

The product and supersession implementation are correct. This repair is state
profile test and evidence work only; it must not change asb-tui or ASB product
code, resolver/channel authority, or the supersession algorithm.

## Required repair

- Express the real invariant independently from one momentary task phase:
  AR-1672 is superseded by existing AR-1668, AR-1668 is done, AR-1673 depends
  on AR-1672, and the upgraded coordinator reports that dependency satisfied.
- Validate every supported AR-1673 phase relevant to this profile:
  `open` is unowned with no lease; `in_progress` has a nonempty owner and
  expiry; `done` is unowned, has no lease, and carries passing spec acceptance
  bound to the declared spec revision.
- Add focused synthetic phase fixtures so all three states and hostile
  owner/lease/acceptance combinations are checked deterministically instead
  of relying only on the state currently checked out.
- Preserve all malformed, missing, self-referential, cyclic, and unfinished
  successor-chain fail-closed cases.
- Run the complete state test suite, vendor verification, headers, generated
  view checks, privacy checks, applicable formal tier, reconciliation, live
  doctor, and hosted Coordination verification at the exact final state head.
- Obtain independent exact-head review. Development authentication, signing,
  DCO, and release publication are warning-only; exact state identity,
  functional evidence, review, and hosted verification remain mandatory.

## Completion boundary

AR-1726 is done only when the final terminal AR-1673 profile passes locally
and in hosted Coordination verification, the authoritative state is clean and
synchronized, and no product repository was modified.
