# AR-1598 — trusted-main coverage regression repair

Repair the post-merge Trusted-main coverage regression introduced by the
catalog-version alignment merge. Add meaningful execution coverage for the
changed protocol/catalog paths and preserve the enforced 90% total threshold;
do not lower thresholds or add broad exclusions.

Dependencies: AR-1593. Downstream: AR-1594 and the fresh-user qualification
series.

Required evidence: local clean coverage at or above the hosted floor, focused
tests for v1.10 negotiation/downgrade and inventory behavior, signed/DCO PR,
independent review, green PR checks, and green exact-main Trusted verification.
