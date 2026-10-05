# AR-1708 — TUI authenticated cassette catalog and strict replay handoff

## Scope

Implement the standalone TUI side of the versioned recording lifecycle:

- decode and validate `RecordingCassetteCatalog` and
  `RecordingReplayDispatch` responses with runner, campaign, generation, and
  digest fencing;
- request the digest-only cassette catalog after authenticated recording
  campaign state is available;
- expose selection-driven strict offline replay from the installed
  `asb tui install` → bare `asb tui` journey;
- preserve the supported top-level command boundary: `asb tui install` must
  materialize the exact qualified TUI bundle and a subsequent bare `asb tui`
  must launch that installed bundle before any catalog, selection, or replay
  action is considered qualified;
- preserve explicit live/local/replay mode labels and typed unavailable or
  stale errors.

No ASB source changes are permitted in this AR. Current main already provides
the pinned v1.12 schema/client and fixtures; if the paired ASB fixture is
unavailable, record that external qualification limitation rather than
inventing a wire shape.

## Acceptance

1. Codec and control-client tests cover valid catalog/replay responses,
   malformed responses, stale runner/campaign/generation identity, digest
   mismatch, unavailable catalog, and replay network-denial behavior.
2. A live authenticated bootstrap requests the catalog once per campaign
   generation and never logs cassette contents or secrets.
3. The TUI can select a digest-only entry and dispatch strict offline replay;
   no implicit fallback to live, mock, or direct filesystem access is allowed.
4. Formal UI model, source/module inventory, help text, and parity checks are
   updated for every new route/action.
5. A clean installed `asb tui install` → bare `asb tui` exact-head receipt
   records the request trace, selected digest, offline boundary, cleanup, and
   paired ASB/TUI identities.
6. The receipt proves that the catalog/replay route was exercised through the
   installed top-level commands, not by invoking an internal binary or helper;
   a direct-binary-only run cannot satisfy this AR.
