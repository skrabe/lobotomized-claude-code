<!--
name: 'Tool Result: MCP complete authentication no flow'
description: >-
  Tells the model no OAuth flow is in progress for the MCP server, that it may
  have timed out, and to call the authenticate tool to start a new one before
  asking the user for the full callback URL
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_NO_FLOW_VAR_0
  - TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_NO_FLOW_VAR_1
  - TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_NO_FLOW_VAR_2
-->
No OAuth flow is in progress for ${TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_NO_FLOW_VAR_0(TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_NO_FLOW_VAR_1)}; it may have timed out. Call \`${TOOL_RESULT_MCP_COMPLETE_AUTHENTICATION_NO_FLOW_VAR_2}\` to start a new one, then, once the user has approved it, ask them for the full URL in their browser's address bar.
