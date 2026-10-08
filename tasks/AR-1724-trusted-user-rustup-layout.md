---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1714",
    "AR-1723"
  ],
  "id": "AR-1724",
  "next_action": "Promote and repair TUI development Cargo discovery for the conventional owner-owned Rustup layout, then rerun the detached exact-main fresh-user journey.",
  "owner": "",
  "plan": "../plans/AR-1724-trusted-user-rustup-layout.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Accept the conventional owner-owned group-writable Rustup development layout with an explicit warning while keeping executable and substitution boundaries fail-closed.",
  "task_revision": 1,
  "title": "Trusted owner Rustup layout and detached quickstart repair",
  "updated_at": "2026-10-08T08:40:00+00:00",
  "worktree_key": ""
}
---

AR-1597 exact-main requalification showed that the standalone TUI returns
`development_tool_unavailable` for the current host conventional Rustup shim:
the shim and resolved toolchain executables are regular, owner-controlled and
non-writable by group/other, while owner-controlled Rustup directories and
`settings.toml` use the common group-writable development layout. Current ASB
already accepts this narrow layout with a visible development warning.

Repair only the standalone `asb-tui` implementation and qualification tools.
Development authentication, signatures, and key management remain visible
warnings and never block local/mock execution. Do not modify ASB product code.

