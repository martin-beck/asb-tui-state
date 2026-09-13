# Agent instructions

Read `docs/DEVELOPMENT.md`, run `tools/handoffctl snapshot`, and read the complete selected task,
plan, dependencies, revision, branch and worktree before acting.

Claim only dependency-ready open work. Route every product, Git, review and publication mutation
through `tools/handoffctl run`. Preserve unrelated work and never reuse another worker's checkout,
branch, owner identity or worktree. Record concise conclusions and immutable public identifiers;
never record prompts, raw logs, credentials, private paths, hostnames or tokens.

This repository uses the Git backend. Task Markdown is authoritative and all transitions must use
`handoffctl`; generated views must not be edited. Commits must be SSH-signed and carry the matching
DCO `Signed-off-by` trailer. Publication requires exact-head checks and independent review.

Do not claim or launch AR-0001 or AR-0002 while pre-existing autonomous asb-tui workers are still
active. Their work must first reach a durable, reviewed handoff and be reconciled without overlap.
