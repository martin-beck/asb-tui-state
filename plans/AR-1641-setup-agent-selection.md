# AR-1641 — Setup agent selection and defaults

Implement selection-driven setup for one or more supported coding agents, persist
their provider/model/auth choices, and allow a shared default for subsequent
runs. Existing configuration remains compatible and development mode stays
non-blocking for absent production credentials.
