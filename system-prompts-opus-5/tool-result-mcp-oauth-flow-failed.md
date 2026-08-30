<!--
name: 'Tool Result: MCP OAuth flow failed'
description: >-
  Tool result when an MCP authenticate stub fails to start the OAuth flow,
  directing the user to /mcp.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_0
  - TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_1
  - TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_2
  - TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_3
  - TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_4
-->
Failed to start OAuth flow for ${TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_0(TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_1)}: ${TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_2(TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_3(TOOL_RESULT_MCP_OAUTH_FLOW_FAILED_VAR_4),200)}. Ask the user to run /mcp and authenticate manually.
