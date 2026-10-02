# AR-1639 — Trusted auxiliary linker resolution

Track TUI compatibility with ASB's bounded auxiliary-linker contract. The
development installation must resolve tools such as `ld` explicitly without
restoring ambient `PATH` or weakening stable/release trust boundaries.

Acceptance:

- The cleared build reproduces and records the missing `ld` failure.
- The ASB repair provides validated absolute auxiliary-linker configuration or
  a private validated wrapper, with no arbitrary environment inheritance.
- Fresh exact-head TUI installation succeeds through materialization.
- Focused/full tests, independent review, hosted checks, and paired lifecycle
  qualification pass.

Development-only authentication, signatures, and key management remain
warning-only and never block this compatibility repair.
