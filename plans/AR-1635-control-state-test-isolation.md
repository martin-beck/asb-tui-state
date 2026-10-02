# AR-1635 — Control-state ownership test isolation

Track the paired qualification dependency on ASB's deterministic control-state
test evidence. No TUI product change is required unless the clean-room run
identifies a real cross-project lifecycle defect.

Acceptance:

- ASB's ownership/recovery test passes focused and hosted gates.
- Paired AR-1632 and AR-1615 qualification runs without cross-test state collisions.
- Development-only authentication, signatures, and key management remain warning-only.
