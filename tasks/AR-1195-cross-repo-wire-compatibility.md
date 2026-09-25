---
{
  "branch": "feature/ar-1195-cross-repo-wire-compatibility",
  "checkpoint_commit": "46fa6f57540c797db4541d50ddb7e91216b253c6",
  "claim_expires": "2026-09-25T14:09:12+00:00",
  "depends_on": [
    "AR-1192"
  ],
  "id": "AR-1195",
  "next_action": "Complete independent exact-head review and cross-repository qualification against ASB catalog/lifecycle pins; do not promote while AR-1192 remains unfinished.",
  "owner": "ar1195-wire-compat",
  "plan": "../plans/AR-1195.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prove asb-tui consumes the exact authenticated ASB catalog and lifecycle wire contracts.",
  "task_revision": 4,
  "title": "Cross-repository wire compatibility",
  "updated_at": "2026-09-25T12:09:12+00:00",
  "worktree_key": "asb-tui-cross-repo-wire-compatibility"
}
---

Replace any independently invented envelope or field model with an exact adapter for ASB's
authenticated JSON-RPC v1.4 catalog and v1.5 lifecycle responses. Preserve canonical digests,
numeric generations, target/libc metadata, closed enums, operation IDs and idempotency bindings.
Keep the UI state machine renderer-neutral and fail closed on schema, digest, identity or version
mismatch.

The implementation candidate is asb-tui PR #86 at exact head
`46fa6f57540c797db4541d50ddb7e91216b253c6`; its retargeted merge head is
`013b381`. It is based on the lifecycle integration branch. The
projection fixes replace the provisional catalog envelope with ASB's authenticated v1.4
JSON-RPC result shape, preserve runner/catalog identity and numeric generations, validate target
and libc/package/provenance fields, enforce closed availability reasons, canonical ordering and
bounds, and validate the catalog digest format. The negotiation fixes reject unsupported versions and
malformed/unknown fields fail closed. The lifecycle qualification fixes decode ASB v1.5 operation
IDs, numeric operation generations, progress/closed states, failure reasons, catalog/runner
bindings and idempotency keys, and encode the exact install request. Checked-in v1.4/v1.5 fixtures,
negative cases, schemas, and renderer-neutral adapter/model tests cover these boundaries.

Independent scope review found only protocol projection, schemas, fixtures, tests, and
renderer-neutral client/model files; no Ratatui, renderer, filesystem/process effects, ASB source,
or coordinator-state changes. GitHub Repository quality run `34948839161` completed SUCCESS for
this exact PR head. This hosted result and focused/full local evidence qualify the candidate
implementation, but do not prove the dependent AR-1192 integration or final `asb tui install`
workflow. A merge blocker remains: the adapter checks that `catalog_sha256` is a syntactically
valid lowercase SHA-256 value but does not recompute the canonical digest from catalog contents or
reject a content/digest mismatch, and the tests do not cover that negative case. AR-1195 therefore
remains planned and dependency-gated until AR-1192 and the ASB v1.4/v1.5 release pins are complete,
canonical digest recomputation/verification is implemented and tested, and an independent
cross-repository exact-head qualification is recorded.

- 2026-09-15T09:05:00+00:00: Updated immutable PR #86 evidence to final head `46fa6f57540c797db4541d50ddb7e91216b253c6`; hosted run `34948839161` passed. Dependency/status intentionally unchanged because AR-1192 is not done.
- 2026-09-15T09:15:00+00:00: Updated PR #86 merge head to `013b381`; retained planned status and AR-1192 dependency. Independent review recorded canonical catalog digest recomputation/content-mismatch testing as a merge blocker.

- 2026-09-25T12:09:05+00:00: AR-1192 is now done; promote AR-1195 for independent digest
  verification and exact-head wire qualification.

- 2026-09-25T12:09:12+00:00: Claimed by ar1195-wire-compat.
