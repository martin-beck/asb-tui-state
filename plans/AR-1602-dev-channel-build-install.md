# AR-1602 — real development-channel clone/build install

Replace the development-channel self-copy shortcut with a bounded temporary
clone/build of the selected ASB-TUI repository head, then atomically publish
only the required launcher and provenance metadata into the private install
root.  Keep `dev` as the default while preserving explicit stable/nightly/
experimental selection and typed unavailable results.  Missing credentials,
signatures, and key-management services remain visible development warnings,
never blockers; stable/production verification remains fail-closed.

Dependencies: TUI AR-1588 plus the released ASB development provenance contract
(ASB AR-1599).  TUI AR-1599 is a downstream paired qualification, not an
implementation prerequisite.  This is the implementation prerequisite
for TUI AR-1600 qualification.

Required evidence: isolated temp clone/build, exact source-head provenance,
bounded cleanup/quotas, atomic publication and rollback, fresh-user install
and rerun, channel matrix, human-readable default output plus `--json`,
independent review, hosted checks, and post-merge paired qualification.
