# AR-1590 — development broker PTY handoff seam

Provide a narrow, validated development-only launcher seam that permits the
asb-tui `run --broker` process to receive its broker descriptor on fd 0 while
using a controlled PTY/terminal for interactive rendering. This seam exists
to make the real ASB↔asb-tui inherited-fd journey testable; it must not alter
stable/production launch behavior or bypass peer, generation, identity, or
transport checks.

Acceptance requires deterministic PTY allocation and teardown, bounded child
and descendant cleanup, terminal-path validation, malformed/disconnect/
timeout negatives, and a real exact-binary integration fixture usable by ASB's
AR-1587 bridge. Development fixtures may use generated local identity and
must not block on production authentication, signatures, or key management.
