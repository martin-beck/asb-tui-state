---
{
  "branch": "feature/ar-1192-authenticated-agent-wizard",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1192",
  "next_action": "Remain blocked only on ASB AR-1316 authenticated agent-catalog producer; provider, model, authentication, defaults, recording and TUI dispatch contracts are now merged and verified.",
  "owner": "",
  "plan": "../plans/AR-1192.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Consume authenticated ASB agent catalog and lifecycle in the standalone wizard.",
  "task_revision": 20,
  "title": "Authenticated agent wizard integration",
  "updated_at": "2026-09-19T17:09:16+00:00",
  "worktree_key": "asb-tui-ar-1192-authenticated-agent-wizard"
}
---

Implement the standalone UI integration in the linked plan after the ASB protocol dependencies are
published. All rendering and application behavior remains in asb-tui.

- 2026-09-15T15:40:43+00:00: Promote for tracking merged renderer-neutral catalog integration and
  remaining authenticated runtime work.

- 2026-09-15T15:40:46+00:00: Claimed by root.

- 2026-09-15T15:40:57+00:00: PR #103 merged into asb-tui main at 249591f after genuine PR CI
  34989446540; post-merge Repository quality 34989738729 and Trusted main verification 34989738764
  both passed. Catalog choices are compatible and bounded; authenticated runtime/install remains
  open.

- 2026-09-15T16:13:38+00:00: Heartbeat by root.

- 2026-09-15T16:14:47+00:00: 2026-09-15 live dependency audit: asb-tui main 9ab1201 and post-merge
  runs 34991922793/34991922837 are green. ASB catalog dependencies AR-1190/1191 are done, but router
  contract AR-1199 is not published; ASB PR #171 head 200edbb has failed Platform evidence run
  34945266711 (native_evidence.py: source identity is not immutable), so authenticated lifecycle
  integration remains gated.

- 2026-09-15T16:22:09+00:00: 2026-09-15 live refresh: ASB lifecycle router PR #157 merged as 967a4a7
  with all listed checks successful; catalog digest PR #174 merged as d354a51. The prior open PR
  #171 is a stale duplicate with a failed synthetic-base platform check and is not a dependency
  candidate. Readiness producer AR-1227 and cross-repo qualification remain unresolved.

- 2026-09-15T16:24:28+00:00: Router audit completed against ASB origin 2117a40: top-level lifecycle
  router PR #157 is merged, but asb-control backend agent_catalog and
  agent_install/status/cancel/retry/remove remain explicit CapabilityUnavailable and Capabilities
  has no lifecycle/catalog fields. The hidden asb-tui v1.5 candidate is not on main and must not be
  imported against rejecting backend. No implementation PR created.

- 2026-09-15T16:29:50+00:00: Heartbeat by root.

- 2026-09-15T16:31:46+00:00: Heartbeat by root.

- 2026-09-15T21:32:35+00:00: Recovered expired claim formerly owned by root. Recover expired root
  lease before re-evaluating ASB backend progress

- 2026-09-15T21:32:52+00:00: Claimed by root.

- 2026-09-15T21:33:12+00:00: 2026-09-15 live refresh: ASB main advanced to 3989cb7 via
  provider-request seam merge, but control.rs still returns CapabilityUnavailable for catalog and
  lifecycle operations. PR #177 head 2d716c8 has checks in progress (architecture, formal, policy,
  Rust, mutation); no exact-head/post-merge backend evidence yet. Recovered expired AR-1192 lease
  and reclaimed it for dependency monitoring.

- 2026-09-15T21:40:02+00:00: 2026-09-15 live update: ASB main advanced to
  efe741a75a8a3e7bd14afd8c6cef119f46a21c74 after PR #177 merged with all 12 checks successful. The
  merged change provides credential enrollment/provider-auth plumbing, not catalog/lifecycle control
  execution. Current ASB source still has explicit CapabilityUnavailable stubs; no safe asb-tui
  implementation slice is available yet.

- 2026-09-16T04:11:59+00:00: Recovered expired claim formerly owned by root. Recover expired
  monitoring lease; ASB progressed only on unrelated replay contract and lifecycle backend remains
  unavailable

- 2026-09-16T11:35:35+00:00: Claimed by codex-asb-tui-ar1192-audit.

- 2026-09-16T11:36:02+00:00: Current asb-tui origin/main was qualified in isolated readiness
  worktree: cargo fmt, clippy, and cargo test --locked pass (136 unit tests plus agent
  catalog/lifecycle, control, selection, renderer, and terminal suites). Existing standalone
  agent_catalog/asb_lifecycle codecs and live projections are bounded and fail-closed. ASB control
  backend still advertises no agent catalog/lifecycle capabilities, so authenticated broker wiring
  cannot safely be completed.

- 2026-09-16T11:36:09+00:00: Blocked by missing ASB agent catalog/lifecycle backend capabilities;
  standalone asb-tui codec/projection implementation is verified and must resume only after ASB
  publishes the authenticated control contract.

- 2026-09-19T17:07:34+00:00: 2026-09-19 read-only dependency audit: asb-tui origin/main is
  adbf14cc21d122f2071c5c2d2dc87754ced24b0f with local locked tests passing; ASB state ea490e4 marks
  AR-1151 done but AR-1160 blocked at 21b675e81191. No TUI-side mutation is authorized until
  authenticated catalog/lifecycle capability is actually published.

- 2026-09-19T17:09:16+00:00: 2026-09-19 follow-up audit: ASB state
  ea490e43003e03eaba075cbc07e00332215fd749 and product main 78a8e9fc2144623311e315fcc4e46c2831b0b2c1
  still expose no agent_catalog or lifecycle capability. ASB AR-1160 checkpoint 21b675e8 remains
  historical blocked; successor AR-1310 is blocked by its DCO/coverage chain. No TUI mutation made.

- 2026-09-21: Current TUI main contains the complete wizard consumer and recording dispatch path,
  but ASB main still returns CapabilityUnavailable for AgentCatalog. Created ASB AR-1316 as the
  bounded producer dependency; no TUI mutation is needed until that contract is published.
