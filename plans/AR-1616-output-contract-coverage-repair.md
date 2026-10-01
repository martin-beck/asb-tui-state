# AR-1616 — trusted coverage repair for the output contract

Restore the existing trusted-main coverage floor after the guided command
output contract is merged. Add behavior-relevant tests for the human-readable
default, explicit JSON selectors, compatibility aliases, malformed input, and
credential-free redaction paths. Do not lower, bypass, or reinterpret the
coverage gate, and do not add tests that merely execute unreachable lines.

Required evidence: exact-main coverage above the existing threshold with
margin, focused output-contract tests, independent review, hosted checks, and
exact-main Trusted verification on the repair merge. Development-only missing
credentials, signatures, and key management remain warnings, never blockers.
