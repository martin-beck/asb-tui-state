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
  "next_action": "Run independent review and hosted checks for coverage repair PR #172 at 21473511c126793522d3f3f77d08772382593c31; merge, then verify Trusted main coverage and release AR-1336.",
  "observed_branch": "feature/ar-1336-launch-live-statistics-clean",
  "observed_dirty": 1,
  "observed_head": "554f20ebb4e8839e956e5b3aca631044c1c63304",
  "owner": "tui-ar1336-dev-20260930",
  "plan": "../plans/AR-1336.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run reviewed benchmark campaigns and show truthful live progress and statistics in the TUI.",
  "task_revision": 76,
  "title": "Benchmark launch and live statistics route",
  "updated_at": "2026-09-30T13:15:28+00:00",
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

- 2026-09-30T12:36:33+00:00: Recorded command exit 0; command argv SHA-256
  57fcd582ee21cb6e1ebd8d17abfda0e3dd631a99861555aab804b705d937e714.

- 2026-09-30T12:38:27+00:00: Independent review found three correctness blockers. PR #170 hosted
  Repository quality also failed DCO because the squashed commit lacked Signed-off-by; repair
  commits must include DCO trailers. AWQ run consequently failed.

- 2026-09-30T12:41:04+00:00: Recorded command exit 0; command argv SHA-256
  8dd21f261129824477f95e288ba7613539dc4f9cfbd1fedf59c722e2321b901d.

- 2026-09-30T12:41:11+00:00: Recorded command exit 0; command argv SHA-256
  c1be3913d5092b699d277de4ec5682393fcc20dd08709284e2476ec82fc5d474.

- 2026-09-30T12:41:22+00:00: Recorded command exit 0; command argv SHA-256
  d9bbebf5bb5731a7c10914c4038138c135215e7b0d76e03fee64419847c05963.

- 2026-09-30T12:41:36+00:00: Recorded command exit 0; command argv SHA-256
  08a3c2db0487713ffe8eca81670782b37270e9ec5690a6535f2f4aac78848a2c.

- 2026-09-30T12:41:58+00:00: Repair PR #171 supersedes PR #170 review blockers: full live catalog
  generation/hierarchy fencing, manual reconnect preservation, terminal immutability. Commit carries
  ED25519 signature and DCO trailer; hosted checks are running.

- 2026-09-30T12:42:20+00:00: Fresh repair branch repair/ar-1336-live-invariants was created from
  PR170 head without altering PR170. Signed commit 869e794 adds live measurement catalog presence,
  generation and digest fencing plus selected group/benchmark/measure membership checks before
  CreatePlan, makes manual reconnect poll failures preserve reconnecting state and retry, and
  rejects all terminal outcome changes without reconciliation. Focused launch tests (7), Cargo
  tests, clippy, UI model/source parity, credential boundary and diff checks pass locally. Commit
  has ED25519 signature SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE and DCO trailer. Fresh PR
  #171 is open; hosted checks are running.

- 2026-09-30T12:43:45+00:00: Fresh review of PR #171 approves terminal immutability and reconnect
  preservation, but blocks merge because benchmark generation is compared to
  snapshot.latest_revision and hierarchy validation relies on ID-string inference. No merge.

- 2026-09-30T12:46:20+00:00: Recorded command exit 0; command argv SHA-256
  424e7ed0313d845d04059d75fcde848ef7ad27fb2face21051a73febdd59a20a.

- 2026-09-30T12:46:29+00:00: Recorded command exit 0; command argv SHA-256
  1a272995752abae32f70e259a6837ef285cb163422c66a8a44b59fd4eae63bb7.

- 2026-09-30T12:46:38+00:00: Recorded command exit 0; command argv SHA-256
  663b34f0d1a2bbadeae3e636737e70788fe3a6513ecf8be405c93d8b243cdce3.

- 2026-09-30T12:46:49+00:00: Recorded command exit 0; command argv SHA-256
  5d9a6fb1ad90532cebcf7241161e249cb6dc2f3df9f8c51d00e70945e2b03ca0.

- 2026-09-30T12:47:15+00:00: Authoritative catalog repair is complete on fresh PR #171. LiveSnapshot
  now carries explicit LiveBenchmarkCatalog with generation, digest, and exact
  pool/group/benchmark/measure membership. Launch validation requires catalog presence, exact
  generation/digest, and traverses selected hierarchy; no latest_revision/debug/prefix heuristics
  remain. Manual reconnect retries after poll errors while preserving reconnecting state. Terminal
  outcomes are immutable. Branch was squashed onto origin/main into one signed+DCO commit 3b672bd.
  Focused launch tests and clippy pass; hosted checks are running.

- 2026-09-30T12:47:29+00:00: Worker force-updated PR #171 with authoritative LiveBenchmarkCatalog
  generation/digest/hierarchy fencing. Commit is ED25519-signed with DCO. Hosted checks restarted.

- 2026-09-30T12:49:08+00:00: Exact PR171 review still blocks merge: benchmark catalog is
  fixture-only because poll_projection has no request/response branch, so normal snapshots reject
  every launch. Hosted quality also hit a flaky synthetic PTY test; rerun after integration repair.

- 2026-09-30T12:54:08+00:00: Recorded command exit 0; command argv SHA-256
  af885912965e6cbf33f88c403dea55ede7624fc665569a496f0303bb4838279e.

- 2026-09-30T12:54:17+00:00: Recorded command exit 0; command argv SHA-256
  e46dce07e402c091578c00b77b71a1f7af1892ea6894268ca7831cfc147ca467.

- 2026-09-30T12:54:28+00:00: Recorded command exit 0; command argv SHA-256
  452942c94c7e0e386d47458971da69c9afe6ba3095e84b2a266cee4e772deb05.

- 2026-09-30T12:54:56+00:00: Live catalog acquisition is now real control-path behavior: added
  version-gated BenchmarkCatalog ControlCall/ControlResult, canonical digest recomputation plus
  bounds/duplicate validation, ControlProjection conversion into LiveBenchmarkCatalog, and
  poll_projection request gated on negotiated V1_7. Added end-to-end projection test for generation
  and hierarchy membership. Commit 63c9945 is ED25519-signed with DCO; prior 3b672bd is also signed.
  Full test suite (231 tests), clippy, and focused projection tests pass locally. PR #171 checks are
  running.

- 2026-09-30T12:55:12+00:00: Added version-gated BenchmarkCatalog control call/result, canonical
  hierarchy digest/bounds validation, live projection acquisition, and integration coverage. Commit
  is ED25519-signed with DCO; hosted checks restarted.

- 2026-09-30T13:00:11+00:00: PR171 merged at 0f1e414 after green PR checks and approval. Trusted
  main verification failed only the coverage threshold (88.92% total); AR remains in progress
  pending repair.

- 2026-09-30T13:04:46+00:00: Recorded command exit 0; command argv SHA-256
  e7e9a8bbeacb8144c7584a9b9e46601f9e8abeb014fc901acfbb9bb8da94b86e.

- 2026-09-30T13:04:55+00:00: Recorded command exit 0; command argv SHA-256
  8278ff084642ac6b712c95829d9d243848f06c59983e68b40d020fcd0b7a24d6.

- 2026-09-30T13:05:06+00:00: Recorded command exit 0; command argv SHA-256
  f4779c7bbbe25134cf68f57cf9f9255754e217278f2cb8284bf06fcbf150d126.

- 2026-09-30T13:05:44+00:00: Post-merge Trusted main failed total coverage at 88.92%. Coverage
  repair PR #172 adds focused canonical catalog and launch-fence tests; local all-target tests pass
  and commit is ED25519-signed with DCO.

- 2026-09-30T13:10:32+00:00: Recorded command exit 0; command argv SHA-256
  d8fae3df7fdc74962ff3ebb3dd47c269e16c101c9c69a53bb9da38f57427a131.

- 2026-09-30T13:10:41+00:00: Recorded command exit 1; command argv SHA-256
  366b291b345f469486ea42a21342a490a58f39a7489fce286a20694599eda1a2.

- 2026-09-30T13:11:13+00:00: Recorded command exit 0; command argv SHA-256
  9715285185c6b8e0235ad20e3fde5a202891a8f9151dc0716fd5e8d4f73d7ba6.

- 2026-09-30T13:15:04+00:00: Recorded command exit 0; command argv SHA-256
  a94e4b2d14d14bdbeba3c8c7369c2fea22df973f13f3f17ecbf16567fd178a23.

- 2026-09-30T13:15:13+00:00: Recorded command exit 0; command argv SHA-256
  8558d0c3da189c73c58e7f1986b24dac79753c4e75eb0a992a796518cf3204a5.

- 2026-09-30T13:15:28+00:00: Recorded command exit 0; command argv SHA-256
  9715285185c6b8e0235ad20e3fde5a202891a8f9151dc0716fd5e8d4f73d7ba6.
