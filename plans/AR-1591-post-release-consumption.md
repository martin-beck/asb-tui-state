---
{
  "id": "AR-1591",
  "title": "Post-release fresh-clone TUI consumption qualification",
  "priority": "P0",
  "depends_on": ["AR-1589", "AR-1590"],
  "summary": "Verify a fresh user can consume the released dev-channel TUI and complete the setup, benchmark, recording, replay, and comparison journey.",
  "status": "planned"
}
---

After the paired backend and TUI implementation ARs are released, use fresh
temporary clones and the published dev channel. Verify install/materialization,
wizard selection of agents/providers/models/defaults, development-only warning
fallback, benchmark execution, recording, offline replay, and comparison.
Capture exact versions, commands, artifacts, and failure explanations. Do not
contact a live provider and do not turn missing auth, signatures, or key
management into a development blocker; stable behavior remains fail-closed.
