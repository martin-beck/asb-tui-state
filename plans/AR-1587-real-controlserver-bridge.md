# AR-1587 real ASB ControlServer bridge

Prerequisite: ASB AR-1592 and paired TUI AR-1592 must establish and qualify
the catalog control contract before this real bridge can claim a complete
bootstrap journey.

Connect the asb-tui ordered bootstrap and mutation journey to a real ASB
ControlServer/backend rather than an in-memory or socket-pair responder. Run
the exact binaries across private roots and the owner-private transport,
negotiate the highest common protocol, and prove ordered catalogs, setup,
authentication, recording, benchmark mutations, identity/digest/revision and
generation fencing, transactional rollback, downgrade behavior, bounded
cleanup, and development-only non-blocking authentication versus stable
fail-closed behavior.
