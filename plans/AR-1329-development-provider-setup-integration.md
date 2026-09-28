# AR-1329 — Development provider setup integration

Bind the development enrollment route into the first-run/reconfiguration wizard
and the provider/model/default selection flow. Support add/edit provider, model
compatibility, set/rotate/reset credential, apply to all or selected agents, and
persist only safe development metadata and defaults.

The route must feed the existing ASB capture/replay contracts and remain
selection-driven. It must label mock/generated credentials and reject live or
offline-incompatible states truthfully.

