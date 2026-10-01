# AR-1583 failure recovery and stable-path regression

Qualify disconnect, timeout, child-crash, stale-generation, malformed-request,
and cancellation recovery with deterministic cleanup and truthful typed errors.
Run the same clean-state checks on the stable/non-development routing path to
ensure development-only allowances do not weaken production boundaries.
