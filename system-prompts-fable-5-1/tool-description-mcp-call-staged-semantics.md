<!--
name: 'Tool description: MCP call staged-call semantics'
description: >-
  Model-facing fragment concatenated into the mcp_call tool description
  explaining STAGED-call lane staging, error subtypes, and redelivery semantics.
ccVersion: 2.1.211
-->

STAGED calls (input_files/output_files declared) additionally stage lane rows in/out around the call — see the `input_files` description. Staged failures come back as a success-subtype response whose staging field carries a typed error_code; subtype:error is emitted only when the call could not be attempted at all (server not connected, kill switch, dispatch failure) and means nothing ran. A target server that is not yet connected is brought up on demand: dispatch runs the deferred plugin/MCP startup resolution (the work a first model turn would have done) and waits up to 30s — shortened by expires_at when that is sooner — for the server to connect before answering "MCP server not connected", so a dispatch that races plugin startup (e.g. after an idle-wake reattach) succeeds instead of failing until a turn runs. Standard RPC semantics: a redelivered request_id supersedes the in-flight run (it is aborted and its response suppressed — exactly one response per request_id). The conversion step is idempotent; this does not mean the target MCP operation is safe to rerun. Cancellable via control_cancel_request.
