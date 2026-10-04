# AR-1701 — TUI live benchmark control and progress

Add the live/local choice and a bounded preflight to the benchmark screen.
Pass the persisted agent/provider/model selection to ASB, show request and
workload progress, cancellation, retry/error details, and final network,
provider, model, and cost metadata. Keep human output concise and expose the
same outcome in JSON. Qualify selected-agent and all-agent fan-out for OpenCode
and OpenDesk through OpenRouter using a replaceable test transport.
