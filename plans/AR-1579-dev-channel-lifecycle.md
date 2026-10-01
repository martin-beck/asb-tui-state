# AR-1579 development-channel lifecycle

Implement and qualify the real `asb tui install --channel dev` lifecycle on a
clean checkout: materialize the current asb-tui main artifact in a temporary
location, record source/tree/digest provenance, and support status, launch,
upgrade, rollback/removal, and repeatable reinstall. Keep development mode
credential-free and non-blocking for production authentication and key
management.
