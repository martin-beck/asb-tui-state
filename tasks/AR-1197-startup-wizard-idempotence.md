---
{
  "branch": "feature/ar1187-startup-idempotence",
  "checkpoint_commit": "6d58181810774d48102eb32bb370a21b101f611f",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1197",
  "next_action": "Review PR #87 at the exact head, then integrate it with AR-1187/#76 and the formal wizard model before promotion.",
  "owner": "",
  "plan": "../plans/AR-1197.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make authoritative startup readiness route into the wizard exactly once when ASB is unconfigured, with deterministic recovery and explanations.",
  "task_revision": 1,
  "title": "Startup wizard readiness and idempotence",
  "updated_at": "2026-09-15T08:25:00+00:00",
  "worktree_key": "asb-tui-ar-1187-startup-idempotence"
}
---

Complete the standalone asb-tui startup contract from AR-1187. Startup must consume an
authoritative ASB readiness response, auto-open the setup wizard only for explicit
`unconfigured` or `incomplete` states, and remain recoverable without fabricating configuration
for unavailable, malformed, stale, or unauthorized responses. Configured startup must remain on
the landing route while retaining a discoverable manual reconfigure action. Keep all application,
navigation, rendering, and formal-model work in asb-tui; ASB owns only its versioned readiness
contract.

The implementation candidate is PR #87, stacked on the readiness classification in PR #76. PR
#87 exact head is `6d58181810774d48102eb32bb370a21b101f611f`; its parent PR #76 exact head is
`1450df452f066dc14f09bef1e7b1a41ec5128032`. The candidate adds the renderer-neutral
`auto_opens_wizard()` and stable explanations, plus deterministic, idempotence, and fail-closed
tests. It deliberately contains no Ratatui renderer or ASB changes.

Completion also requires integration with the formal AR-1182/1184 state and transition model,
ownership/CI checks, wizard completion confirmation, reconnect/resize/restart behavior, and
TestBackend/model/property evidence for configured, unconfigured, incomplete, unavailable,
malformed, stale, unauthorized, cancel, completion, and manual reconfiguration paths. Do not
promote or merge until exact-head review, hosted CI, SSH signature/DCO checks, and the dependent
wizard work are complete.
