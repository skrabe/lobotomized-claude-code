<!--
name: MCP Wait Connected Repl
description: >-
  Wait-for-servers tool result listing MCP servers whose tools are callable only
  inside the REPL, not as top-level tools.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_MCP_WAIT_CONNECTED_REPL_VAR_0
-->
Connected (their tools are now callable inside the REPL environment — not as top-level tools): ${TOOL_RESULT_MCP_WAIT_CONNECTED_REPL_VAR_0.connected.join(", ")}
