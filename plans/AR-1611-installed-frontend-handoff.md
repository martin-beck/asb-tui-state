# AR-1611 — installed frontend handoff and dev-channel launch

Define the versioned handoff consumed by an installed asb-tui binary: exact
ASB control endpoint, selected channel, manifest/source digest, workspace/state
roots, and development-mode warning status. Launch must be restart-safe,
diagnose incompatible manifests in plain language, and preserve the previous
known-good executable when an update fails. Default output is human-readable;
`--json` is opt-in.
