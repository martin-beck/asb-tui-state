# AR-1697 — Repair channel AR specifications and current-head qualification

Repair the coordination metadata for the TUI channel release path. Normalize
the AR-1674 and AR-1675 specifications to the supported schema and preserve
their explicit development-only warning boundary. Then rerun the paired
channel and quickstart evidence against the current ASB/TUI heads.

Acceptance:

- AR-1674 and AR-1675 specs parse, have complete predicates, evidence classes,
  and gates, and retain their original intent.
- The exact paired rerun binds ASB `ad43609b67825f7f422b371f5d8104e0a5b20f2e`
  and TUI `1cf4b43d7c6e8782179bbdd448d8ae14aa91fb34`.
- Selection, manifest diagnostics, lifecycle matrix, and channel-aware
  setup-to-offline-analysis evidence are recorded with privacy-safe digests.
- No predecessor AR is marked done unless handoffctl dependency readiness and
  its own receipt predicates permit that transition.
- Missing development authentication, signatures, and key management remain
  visible warnings and never block.
