<!--
name: MCP Wait Cached Repl
description: >-
  Wait-for-servers tool result listing cached MCP servers whose tools become
  callable inside the REPL on first call.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_MCP_WAIT_CACHED_REPL_VAR_0
-->
Cached (their tools are callable inside the REPL environment now; connects on first call): ${TOOL_RESULT_MCP_WAIT_CACHED_REPL_VAR_0.cached.join(", ")}
