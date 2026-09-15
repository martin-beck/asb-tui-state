---
{
  "branch": "feature/ar1037-help-ci-hardening",
  "checkpoint_commit": "74e05d8bb262260f1cef2375ca70800b208bedb6",
  "claim_expires": "2026-09-15T09:12:55+00:00",
  "depends_on": [],
  "id": "AR-1198",
  "next_action": "Complete independent review against UI_OWNERS, UI-module inventory, formal model, and all UI routes; PR #88 exact head 74e05d8bb262260f1cef2375ca70800b208bedb6 remains unpromoted.",
  "owner": "root-ar-tui-registry",
  "plan": "../plans/AR-1198.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make document-backed contextual help complete, meaningful, privacy-safe, and continuously enforced by CI.",
  "task_revision": 7,
  "title": "Contextual-help catalog CI hardening",
  "updated_at": "2026-09-15T08:52:58+00:00",
  "worktree_key": "asb-tui-ar-1037-help-ci-hardening"
}
---

Implement and qualify the standalone asb-tui help contract from AR-1037 and the related help
catalog work. The catalog must be a versatile, document-backed structure that can be extended for
new screens, elements, actions, and context without scattering prose through rendering code.
Every user-facing UI element and every performable action must resolve to meaningful, plain,
privacy-safe helper text appropriate to its current context; unknown IDs, missing entries, wrong
entry kinds, malformed documents, schema drift, host paths, credentials, and secret-like material
must fail closed.

The implementation candidate is PR #88 at exact head
`74e05d8bb262260f1cef2375ca70800b208bedb6` (asb-tui, based on AR-1037/#61 and related catalog
AR-1036/#60). It changes only help validation/tests and contains no ASB, Ratatui, renderer, or
application implementation. Hosted Repository quality run `34948910240` passed. The candidate
validation commands are `python3 tools/validate-ui-help.py`, `python3 tools/test-ui-help.py`,
`cargo +1.93.0 fmt --all -- --check`, `cargo +1.93.0 clippy --locked --all-targets -- -D warnings`,
and `cargo +1.93.0 test --locked --all-targets`.

Completion requires exact-head review, SSH signature and DCO verification, hosted CI, and
cross-checking the catalog against UI_OWNERS, the UI-module inventory, formal state/elements/
transitions, contextual hotkey/help requirements, and all wizard/landing/configuration/report
routes. CI must detect every newly introduced UI element or action lacking meaningful helper text;
tests must cover schema drift, unknown actions, wrong kinds, private material, missing context,
and deterministic lookup. Do not merge or promote until these checks and durable evidence are
recorded. All actual UI application and rendering work remains in asb-tui.

- 2026-09-15T09:00:00+00:00: Registered from PR #88 at exact head `74e05d8bb262260f1cef2375ca70800b208bedb6`; hosted run `34948910240` passed and the candidate reports the focused/full validation commands above.

- 2026-09-15T08:51:46+00:00: Claimed by root-ar-tui-registry.

- 2026-09-15T08:52:03+00:00: Recorded command exit 0; command argv SHA-256
  0813568ea80c6e65465602e50685396e79e1b48c7baac282f5bff0485d30674c.

- 2026-09-15T08:52:30+00:00: Independent source review: PR #88 exact head
  74e05d8bb262260f1cef2375ca70800b208bedb6 changes only tools/test-ui-help.py and
  tools/validate-ui-help.py; no ASB, Ratatui, renderer, or application implementation. GitHub
  Repository quality run 34948910240 completed SUCCESS. Focused diff covers unknown top-level
  fields, unknown action IDs, wrong action kinds, placeholder/private-material rejection and
  deterministic negative tests. This is evidence for the candidate checks, not proof of complete UI
  inventory synchronization or all-context coverage; those remain acceptance gates.

- 2026-09-15T08:52:32+00:00: Released after exact-head source review and hosted-check verification;
  retain as open until complete UI inventory/formal-model/ownership cross-check and independent
  promotion review.

- 2026-09-15T08:52:55+00:00: Claimed by root-ar-tui-registry.

- 2026-09-15T08:52:58+00:00: Recorded command exit 0; command argv SHA-256
  0813568ea80c6e65465602e50685396e79e1b48c7baac282f5bff0485d30674c.
