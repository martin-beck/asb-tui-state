# AR-1689 — paired TUI fresh-user integration and receipt qualification

Run one disposable exact-head journey: install current dev channel, open the
TUI wizard, select agents/provider/model/workload, generate a content-addressed
plan, execute a mock benchmark, record selected/all responses, replay offline,
compare, and inspect analysis.

## Acceptance

- Setup selections reach ASB plan creation without hand-authored identity data.
- Positive benchmark, recording, strict offline replay, comparison, and
  analysis evidence is complete.
- Stale identity, unavailable provider, incomplete cassette, and no-network
  cases fail with actionable typed diagnostics.
- Receipt records exact ASB/TUI heads and digests, contains no secrets, and
  distinguishes development warnings from blockers.
- Hosted checks, independent review, generated projections, and post-merge
  exact-head verification pass.
