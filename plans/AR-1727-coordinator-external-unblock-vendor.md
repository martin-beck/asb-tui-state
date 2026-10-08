# AR-1727 plan: vendor Coordinator external-unblock repair

1. Acquire a clean exact upstream Coordinator checkout at merge
   `ee68fbd31ef5564586e4e81297a175abcaa49c6d` and verify tree
   `77803e514ec9384ec623b5b65deb5356165981ad`, ancestry, PR #1199 review, and
   exact-main Verify/Formal results.
2. Run the official `tools/vendor.py sync-development` path into this state
   repository. Review the complete diff and mechanically verify all blobs,
   hashes, modes, manifest fields, and unchanged downstream binding/backend/
   profile files. Never patch a vendored path directly.
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
