---
{
  "branch": "feature/ar-1336-launch-live-statistics",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-30T13:53:30+00:00",
  "depends_on": [
    "AR-1335",
    "AR-1323"
  ],
  "id": "AR-1336",
  "next_action": "Run independent exact-head review and hosted CI for PR #170 at 402ec56db350655f8d688ac17c3924d9b2651462; merge only after both pass, then watch main post-merge checks.",
  "observed_branch": "feature/ar-1336-launch-live-statistics-clean",
  "observed_dirty": 1,
  "observed_head": "554f20ebb4e8839e956e5b3aca631044c1c63304",
  "owner": "tui-ar1336-dev-20260930",
  "plan": "../plans/AR-1336.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run reviewed benchmark campaigns and show truthful live progress and statistics in the TUI.",
  "task_revision": 44,
  "title": "Benchmark launch and live statistics route",
  "updated_at": "2026-09-30T12:34:51+00:00",
  "worktree_key": "asb-tui-ar-1336-launch-live-statistics"
}
---

Development fixtures may run without external authentication or provider reachability; production qualification remains separate.

- 2026-09-30T11:53:22+00:00: Dependencies AR-1335 and AR-1323 are done; begin generation-bound
  launch, cancellation, reconnect, and live statistics implementation.

- 2026-09-30T11:53:30+00:00: Claimed by tui-ar1336-dev-20260930.

- 2026-09-30T11:54:38+00:00: Recorded command exit 0; command argv SHA-256
  fbfb43790675e20337beb2a62d4de0c20f442547b30357e99eb69befb55cf993.

- 2026-09-30T12:04:20+00:00: Recorded command exit 0; command argv SHA-256
  39e1e9452bcd7db7441450bfe7c82ff432354899cf413c7b577cc49feaeb85ff.

- 2026-09-30T12:04:29+00:00: Recorded command exit 0; command argv SHA-256
  e57c522dedf195cfccc6bfa23a107de262c374cce29392634d92f6487d0b26e5.

- 2026-09-30T12:04:45+00:00: Recorded command exit 0; command argv SHA-256
  4521141c1b99dec4dc314a4293a7108b267234bec0c586165ce4593fe40487ca.

- 2026-09-30T12:04:58+00:00: Recorded command exit 1; command argv SHA-256
  03831a502f8484a3dabc033b8f515a942e6554f0ad0133a45b626fa00f549ff8.

- 2026-09-30T12:05:21+00:00: Recorded command exit 0; command argv SHA-256
  03831a502f8484a3dabc033b8f515a942e6554f0ad0133a45b626fa00f549ff8.

- 2026-09-30T12:05:52+00:00: Implemented generation-bound launch validation before control I/O,
  reviewed materialized plan creation and launch, explicit start/cancel/reconnect controls, bounded
  live refresh, and truthful provenance-aware live statistics state with stale-event and reconnect
  fencing. PR #165 is open at exact head 877996906a15a85243bfc681d188b49ec5cd6a6e; local cargo
  tests/clippy and UI gates pass.

- 2026-09-30T12:06:42+00:00: Recorded command exit 1; command argv SHA-256
  3f59e5ea84562fcbd5d497d5d8022fdd7e0e87307de3c0762fcbfee5ad507176.

- 2026-09-30T12:07:28+00:00: Recorded command exit 0; command argv SHA-256
  045f28a3a319af0c5d38130baaa6b0b4eb179a7da56e325935b792ae84edfa22.

- 2026-09-30T12:07:38+00:00: Recorded command exit 0; command argv SHA-256
  92a0077746a51eeabbabcc77c972ff0cf5298fb05b305be6499fe3c066fbfe29.

- 2026-09-30T12:08:19+00:00: Rebased AR-1336 onto current main 5bc08b7 after AR-1335 follow-up
  landed; amended with SSH signature and force-with-lease pushed exact head
  4fa5c61cb681fe4c229fc7810e9ef9e7befdef61. PR #165 workflows are running (Repository quality run
  36712806539 and AWQ shadow run 36712807064).

- 2026-09-30T12:13:33+00:00: Recorded command exit 0; command argv SHA-256
  d898bfb31da7db2bc862de89c1dcc0cb0e8005a18d66f936a2b85d197048d415.

- 2026-09-30T12:13:41+00:00: Recorded command exit 0; command argv SHA-256
  4c81881f7613daef5bf42c40162a0fa8748b9a5e94b03d744d2029434386c26c.

- 2026-09-30T12:13:52+00:00: Recorded command exit 0; command argv SHA-256
  6509c565a69d3bdef26745d39741d8155b7db12057ad47895bd585aa3c64fc60.

- 2026-09-30T12:14:30+00:00: Formal-model repair committed and pushed as signed 0a37121: run-control
  start_run, cancel_run, and reconnect transitions plus focused executable test; WorkspaceState
  gates emitted actions through the formal model. Full cargo test, clippy, UI model/source parity,
  credential boundary, and diff checks pass locally. PR #165 now points to exact head 0a37121;
  hosted checks have not started yet.

- 2026-09-30T12:15:16+00:00: Recorded command exit 0; command argv SHA-256
  02d2b2fed07d78b72d231d3fdb44b24907d4555c3aa346f1090e573a8430b9fe.

- 2026-09-30T12:15:26+00:00: Recorded command exit 0; command argv SHA-256
  0b507c7db2afb4e3ba5a9d223229e3c81000bb3cabdac3eaea743109dd6861a9.

- 2026-09-30T12:15:57+00:00: PR #165 was safely closed/reopened to retrigger pull_request workflows
  after the signed formal-model repair, but GitHub still reports no checks or runs for head 0a37121;
  only old failed runs at 4fa5c61 exist. Local implementation and all gates remain green.

- 2026-09-30T12:19:12+00:00: Rebased signed AR-1336 implementation onto current main as PR #168
  after the original branch Actions trigger anomaly. Clean head c626fc2 includes LaunchBinding
  validation, generation-bound launch/cancel/reconnect, truthful live statistics, and formal
  lifecycle tests; local 225-test/clippy/model/parity/credential checks pass.

- 2026-09-30T12:23:57+00:00: Recorded command exit 0; command argv SHA-256
  e230bdc474e11cc5790490407aa8586737572d74d5b8d834bd704044933b58ce.

- 2026-09-30T12:24:06+00:00: Recorded command exit 128; command argv SHA-256
  1a90c4772591393c20eff5fcdb38045982367afbe88a1198ac99af5317fc83a5.

- 2026-09-30T12:27:53+00:00: Recorded command exit 0; command argv SHA-256
  d6ab3f562b5fedd95b83622bf6fe71d05a29558bfe290b887b657c8ff7890c6d.

- 2026-09-30T12:28:01+00:00: Recorded command exit 0; command argv SHA-256
  b09f31dda8a050af71b14691f7b05c27048a44dc7f9c20b24b0d5af031300455.

- 2026-09-30T12:28:13+00:00: Recorded command exit 0; command argv SHA-256
  d140073cd09ac4493342ccf67150848850f7a0399a7c41891974c7996db75481.

- 2026-09-30T12:29:21+00:00: Recorded command exit 0; command argv SHA-256
  e107cd262c72426e0bce2fbcb1215ca2f094f6fb05151fe29a1113ec851d40a8.

- 2026-09-30T12:29:30+00:00: Recorded command exit 0; command argv SHA-256
  875b2bbf70832e33bef920a484638fa306aacfe09a034ea1682c460b251a452d.

- 2026-09-30T12:29:40+00:00: Recorded command exit 0; command argv SHA-256
  6509c565a69d3bdef26745d39741d8155b7db12057ad47895bd585aa3c64fc60.

- 2026-09-30T12:30:11+00:00: All four independent review blockers are implemented in signed commits
  9efaa4a and 554f20e: canonical MaterializedBundle integrity and benchmark selection validation
  precede CreatePlan, poll failures preserve LaunchState statistics while entering reconnecting,
  terminal states reject nonterminal regressions, and cancellation targets LaunchState exact
  run/attempt IDs. Full cargo tests (227 library plus integration), clippy, UI model/source parity,
  credential boundary and diff checks pass locally. Both commits verify with ED25519 key
  SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE. PR #168 head is 554f20e; GitHub reports no new
  checks after push.

- 2026-09-30T12:34:46+00:00: PR #168 trigger anomaly was bypassed with fresh PR #170 from current
  main. Local cargo fmt and all-target tests pass (229 library tests plus integration targets);
  commit is ED25519-signed. Hosted checks and fresh review pending.
