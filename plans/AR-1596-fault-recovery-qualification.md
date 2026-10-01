# AR-1596 — fault and recovery qualification

Consume the ASB fault-matrix runner and qualify TUI recovery for stale
generation, unsupported model/provider, missing credentials, cassette faults,
timeouts, cancellation, crash, and cleanup. Keep warning-only development
fallbacks visibly distinct from production failures.

Dependencies: AR-1595 and paired ASB AR-1597. Downstream: AR-1597.

Required evidence: matrix-linked TUI cases, bounded retry/cleanup, exact-head
receipts, signed/DCO PR, independent review, and hosted checks.
