# AR-1345 final exact-head qualification

Date: 2026-10-01

## Exact inputs

- ASB commit: `852dcb14f9c19b1663b5b95c3b4d39f9fb8fe52e`
- ASB tree: `fcb82399d8fbe90e36505e96a02c6d206857d582`
- asb-tui commit: `474f9fc9b32e546be89cb2d5a321328c716aacce`
- asb-tui tree: `fed3a2a3d0426c30ca7391f3f506d3f5a1ed594b`
- Both qualification worktrees were clean detached exact-head worktrees.

## Evidence

Exact-head builds/tests passed:

- ASB `cargo test --locked -p asb-cli`: 147 unit tests and all package integration suites passed.
- asb-tui `cargo test --locked --lib development_broker`: 3 descriptor tests passed.
- asb-tui `cargo build --locked --bin asb-tui` passed.

The valid dynamic descriptor contained the four exact identities above, development profile, `development_only=true`, operation `launch`, and protocol minor 10. Running `asb-tui run --broker --development` with all four expected-identity environment values returned exit 2 with `broker channel adoption failed`; this proves descriptor acceptance reached the inherited broker/socket boundary. No socket was supplied in the disposable probe.

Negative probes returned exit 3 and `development broker descriptor rejected`:

- malformed `{}` descriptor;
- stale ASB commit identity;
- unsupported protocol minor 9.

Fresh clean-home lifecycle probes were privacy-safe and network-free where applicable:

- status: exit 3, typed `extension_not_installed`;
- doctor: exit 0, truthful `extension_not_installed`;
- remove: exit 3, typed `extension_not_installed`;
- offline development install: exit 4, network `denied`, typed `trusted_tool_unavailable`.

## Blocker

Fresh development materialization cannot start on this host. The only `cargo`
is the user-home `.cargo/bin/cargo`, a user rustup shim under group-writable
ancestors (`.cargo` and `bin` mode 775); `/usr/bin/cargo` is absent. The
trusted development resolver correctly rejects that tool and returns
`trusted_tool_unavailable`. A secure standalone cargo/rust toolchain is needed
to qualify actual clone/build/materialization and subsequent installed
status/launch/remove transitions. No production authentication, signatures,
or key-management requirement caused the failure.

Conclusion: broker descriptor compatibility and negative paths pass, but the
complete first-time development journey is **blocked** by the host toolchain
prerequisite; AR-1345 must not be marked done.
