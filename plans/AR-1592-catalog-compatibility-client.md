# AR-1592 — TUI catalog compatibility client

Audit the released TUI bootstrap's `BenchmarkCatalog` and
`MeasurementCatalog` requests against the ASB AR-1592 protocol implementation.
Repair only client-side version intersection, downgrade/fallback, validation,
and user-facing error handling needed for the common contract. Keep the real
ASB bridge and inherited-fd proof in AR-1587/AR-1590.

Required evidence:

- ordered typed bootstrap request/response assertions;
- negotiated-version and unsupported-call negatives;
- identity, revision, digest, and stale-publication validation;
- bounded cleanup and development non-blocking auth behavior;
- exact signed/DCO PR, independent review, and green hosted checks.

Dependencies: AR-1586. Cross-project input: ASB AR-1592. Downstream: AR-1593
and AR-1587. This client-validation slice may release independently; the
cross-version negotiation mismatch is explicitly owned by AR-1593.
