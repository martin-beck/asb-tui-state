# AR-1703 — Top-level `asb tui install` and `asb tui` qualification

## Scope

This asb-tui AR owns the downstream qualification of the supported top-level
commands. It does not add ASB source or duplicate ASB lifecycle authority.

The exact paired development channel must be exercised through:

```text
asb tui install
asb tui
```

The test must prove that installation materializes the intended asb-tui
artifact, that the subsequent top-level launch reaches that installed artifact,
and that the full selection-driven wizard remains usable from that entrypoint.

## Acceptance criteria

1. A clean disposable home can run `asb tui install` with the default
   development channel, receive typed human and JSON diagnostics, and retain
   exact source/artifact provenance.
2. A subsequent `asb tui` launch starts the installed asb-tui application,
   preserves the development-only warning policy, and opens the wizard only
   when no configuration exists; configured users reach the landing screen.
3. The journey covers provider/model/agent selection, benchmark and measure
   selection, live-run handoff, selected/all recording, strict offline replay,
   comparison, restart, removal, and actionable failures without asking the
   user to copy internal paths or arguments.
4. The same command paths are checked in human and machine-readable modes where
   supported, including missing toolchain, stale/tampered artifact, absent
   terminal, and unavailable-provider diagnostics.
5. The receipt records exact ASB and asb-tui heads, installed executable digest,
   command transcripts, cleanup result, and whether each result is development
   qualification or production release evidence. No production release claim
   may be made from a development fixture.

## Dependencies

The implementation and feature ARs must be complete before this qualification
is promoted: AR-1575, AR-1654, AR-1700, AR-1701, and AR-1702. AR-1575 is the
paired live-materialization gate; bundle-only or directly invoked binary
evidence does not replace a successful `asb tui install` followed by a
terminal-capable bare `asb tui`. Any ASB-side command or protocol defect is
reported as an external dependency; this AR must not modify the ASB repository.
