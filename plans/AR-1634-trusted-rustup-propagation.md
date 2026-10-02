# AR-1634 Trusted development rustup propagation

Coordinate the TUI-side contract for ASB's bounded trusted rustup propagation:
the current TUI main source must build from a validated user-owned rustup home
after ASB clears child environments, while unsafe PATH/toolchain roots remain
rejected. Qualify fresh install, status, upgrade, and remove with local/mock
fixtures and no production authentication chain.

Missing development authentication, signatures, and key management remain
warning-only and never block development.
