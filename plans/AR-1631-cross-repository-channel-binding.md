# AR-1631 Cross-repository development-channel binding

Bind the separately published asb-tui lifecycle to ASB's explicit release
channel contract. A fresh `dev` install must retain the selected channel in
TUI status, launch, upgrade, restart, and JSON projections while unsupported
channels remain typed unavailable choices.

Generated development credentials/signatures are acceptable. Missing
authentication, signature validation, and key management remain visible
warnings and never block development.

Acceptance: exact current-main ASB and TUI heads pass paired channel
propagation and unavailable-channel contract tests with hosted checks green.
