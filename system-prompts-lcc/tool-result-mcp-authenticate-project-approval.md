<!--
name: 'MCP Authenticate: Project Approval Required'
description: >-
  MCP authenticate tool call() error result when the server still needs project
  approval; do not retry until the user approves.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_MCP_AUTHENTICATE_PROJECT_APPROVAL_VAR_0
  - TOOL_RESULT_MCP_AUTHENTICATE_PROJECT_APPROVAL_VAR_1
-->
${TOOL_RESULT_MCP_AUTHENTICATE_PROJECT_APPROVAL_VAR_0(TOOL_RESULT_MCP_AUTHENTICATE_PROJECT_APPROVAL_VAR_1)}. Ask the user to approve it; do not retry until they have.
