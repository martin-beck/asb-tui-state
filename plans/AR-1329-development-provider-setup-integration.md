# AR-1329 — Development provider setup integration

Bind the standalone development enrollment route into the first-run/reconfiguration
wizard (paired with the ASB AR-1499 and AR-1500 contracts), without depending on
the live authenticated router or helper qualification.
and the provider/model/default selection flow. Support add/edit provider, model
compatibility, set/rotate/reset credential, apply to all or selected agents, and
persist only safe development metadata and defaults.

The route must feed the existing ASB capture/replay contracts and remain
selection-driven. It must label mock/generated credentials and reject live or
offline-incompatible states truthfully. Missing authentication, signature
validation, or key management must not prevent development setup or local mock
benchmarking; the UI presents a warning and continues with the generated fixture.
