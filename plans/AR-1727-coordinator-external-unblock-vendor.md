# AR-1727 plan: vendor Coordinator external-unblock repair

1. Acquire a clean exact upstream Coordinator checkout at merge
   `e863b57edc7f7a21b2aff2c7b45ce226e12637d2` and verify tree
   `eee603591b917eeca244425559d7c67bb88a7268`, ancestry, PR #1200 review, and
   exact-main Verify/Formal results. Retain topic commit `f003d25e1ff99f30c24853553d1d72ebf0211657`
   only as reviewed candidate provenance.
2. Run the official `tools/vendor.py sync-development` path into this state
   repository. Review the complete diff and mechanically verify all blobs,
   hashes, modes, manifest fields, the 68-file closure, manifest SHA-256
   `d210d9a1b54cedafa1b721718f6661cf46d87d54757186d26a8fc11868ab2d43`, and
   unchanged downstream binding/backend/profile files. Never patch a vendored path directly.
3. Add only downstream profile coverage needed to exercise a real
   release-blocked fixture, subsequent claim, genuine paused resume, hostile
   provenance, and the existing supersession/terminal-lifecycle contracts.
4. Run vendor verification, headers, the full state unit suite, generated-view
   and privacy checks, formal portable-smoke and PR-publication tiers,
   reconciliation, snapshot, and live doctor.
5. Commit the state-only candidate, obtain independent exact-head review,
   repair all findings, and require terminal-green hosted Coordination
   verification on the final accepted SHA.
6. Record a privacy-safe receipt and spec acceptance, release AR-1727 done,
   reconcile, and verify post-release hosted CI and live doctor.
7. Use the supported exact-revision `unblock` command on AR-1575; do not edit
   its task or session log. Hand AR-1575 to its qualification worker only after
   the transition is durably synchronized.
