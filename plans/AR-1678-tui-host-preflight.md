# AR-1678 — TUI development install host preflight and typed recovery

Expose a disposable preflight before the TUI materializes the default `dev`
channel. Check bounded toolchain, PTY, filesystem, and linker prerequisites,
show stable remediation in the TUI, and preserve the same typed result in JSON.
Distinguish a host limitation from a product failure, and verify retry,
cleanup, rollback, and channel persistence in an exact-head receipt.

Absent provider credentials and development-only authenticity/key warnings must
remain visible but non-blocking.
