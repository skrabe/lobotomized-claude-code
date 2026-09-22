<!--
name: 'MCP Wait Result: Cached Servers'
description: >-
  Line assembled inside `mapToolResultToToolResultBlockParam` of the MCP Wait
  For Servers tool, listing servers whose tools are already usable and which
  connect on first call; returned to the model as the tool result.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_MCP_WAIT_CACHED_VAR_0
-->

Cached (their tools are available now; connects on first call): ${TOOL_RESULT_MCP_WAIT_CACHED_VAR_0.cached.join(", ")}
