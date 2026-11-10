<!--
name: 'Tool Result: MCP OAuth redirect guard (cross-origin)'
description: >-
  Error thrown when an MCP OAuth request is redirected to another origin;
  reaches the model inside the MCP authenticate tool's 'Failed to start OAuth
  flow' result.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_0
  - TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_1
  - TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_2
-->
Stopped an OAuth request, which can hold secrets: ${TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_0(TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_1)} redirected it to ${TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_0(TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_2)}. Ask the owner of ${TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_0(TOOL_RESULT_MCP_OAUTH_REDIRECT_GUARD_CROSS_ORIGIN_VAR_1)} to remove that redirect.
