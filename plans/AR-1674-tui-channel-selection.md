# AR-1674 — TUI channel selection and persisted default

Add a first-class channel step to initial setup and reconfiguration. `dev` is
selected when no value exists; the choice is persisted and rendered in the
landing, status, install, upgrade, and launch views. Unknown or unavailable
channels must explain the failure and must not silently become `dev`.

Acceptance covers keyboard navigation, restart persistence, human/JSON output,
and visible development-only warning states without an authentication gate.
