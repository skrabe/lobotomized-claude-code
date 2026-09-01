<!--
name: 'MCP wait: server not configured'
description: >-
  Fragment of the wait-for-MCP-servers tool result returned to the model listing
  servers with no URL set that the user must configure first.
ccVersion: 2.1.210
variables:
  - TOOL_RESULT_MCP_WAIT_SERVER_UNCONFIGURED_VAR_0
-->
Not configured (no URL set — retrying will not help; the user must configure the server first): ${TOOL_RESULT_MCP_WAIT_SERVER_UNCONFIGURED_VAR_0.unconfigured.join(", ")}
