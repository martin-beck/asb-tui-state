# AR-1721 — Operator quickstart controlling-PTY runner

Repair `tools/run-operator-quickstart.py` so its public-boundary launch is a
faithful, bounded interactive-terminal qualification rather than a file-
descriptor-only pseudo-terminal fixture.

## Scope

1. Start each interactive launch as a session leader with the PTY slave as its
   controlling terminal and foreground process group. Avoid thread-unsafe
   `preexec_fn` shortcuts; use an auditable bounded launcher mechanism.
2. Set and verify a nonzero initial terminal size before exec. Exercise a normal
   operator-sized terminal, not a zero-row/zero-column compatibility accident.
3. Drive the launch with bounded reads and writes, send the documented quit
   action only after readiness, and impose explicit handshake, interaction, and
   process-exit deadlines.
4. On timeout or protocol failure, terminate and reap only the authenticated
   fixture process tree, close both PTY ends, and retain a privacy-safe typed
   diagnostic. Do not leave descendants or terminal state behind.
5. Preserve strict JSON extraction, human-output checks, exact binary/source
   identity binding, local-bundle installation, credential stripping, and
   network-denied downstream qualification.
6. Add focused positive and negative tests proving controlling-terminal
   ownership, foreground-group identity, nonzero window size, bounded quit,
   timeout cleanup, malformed/no-JSON handling, and secret-free receipts.
7. Re-run the exact paired `asb tui install` then bare `asb tui` operator journey
   after the separate ASB development-broker foreground-terminal repair lands.

## Boundaries

This AR owns only the asb-tui qualification runner and its contract tests. The
actual application stays in the asb-tui repository unchanged by this repair;
ASB owns the development-broker process-group and foreground-terminal fix. No
mock success, direct internal-binary substitute, host-network fallback, or
production trust relaxation may satisfy the public command journey.

