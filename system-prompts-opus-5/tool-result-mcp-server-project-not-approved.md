<!--
name: 'Tool Result: MCP Server Project Not Approved'
description: >-
  MCP authenticate tool result when a project-scope .mcp.json server is not
  approved for this project, telling the model to wait for the user to approve
  it.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_MCP_SERVER_PROJECT_NOT_APPROVED_VAR_0
  - TOOL_RESULT_MCP_SERVER_PROJECT_NOT_APPROVED_VAR_1
-->
"${TOOL_RESULT_MCP_SERVER_PROJECT_NOT_APPROVED_VAR_0(TOOL_RESULT_MCP_SERVER_PROJECT_NOT_APPROVED_VAR_1)}" is a project-scope MCP server (.mcp.json) that is not approved for this project — approve it via /mcp first, then authenticate or reconnect it
