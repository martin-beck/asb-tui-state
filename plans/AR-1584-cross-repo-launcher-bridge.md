# AR-1584 cross-repository launcher and bridge

Implement the real ASB-to-asb-tui development launcher/bridge: owner-private
socket/channel discovery, exact executable and source identity binding, peer
credential checks, inherited fd/SCM_RIGHTS transfer, broker packet handoff,
bounded child lifetime, and deterministic cleanup. Cover the actual `asb tui`
launch path rather than only fixture/module seams.
