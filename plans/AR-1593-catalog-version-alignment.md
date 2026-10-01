# AR-1593 — TUI catalog protocol version alignment

Make the TUI and ASB agree on the catalog-capable protocol version. Extend the
TUI only as far as the ASB contract requires, preserving every older immutable
schema and explicit unsupported-version negative. Update PR #191 or publish a
successor with exact negotiation, downgrade, and real bootstrap evidence.

Required evidence:

- published version matrix and common-version selection;
- v1.12 (or documented common replacement) codec/schema support;
- downgrade behavior that omits unsupported catalog calls explicitly;
- stale/identity/digest validation and bounded cleanup;
- signed/DCO PR, independent review, and green hosted checks.

Dependencies: asb-tui AR-1592 and ASB AR-1592. Downstream: asb-tui AR-1587.
