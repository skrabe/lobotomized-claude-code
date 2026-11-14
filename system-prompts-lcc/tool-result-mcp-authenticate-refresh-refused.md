<!--
name: 'Tool Result: MCP authenticate refresh refused'
description: >-
  Tells the model the sign-in server refused the last token refresh of an MCP
  server and to ask the user to run /mcp reconnect or /mcp to sign in again
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_AUTHENTICATE_REFRESH_REFUSED_VAR_0
  - TOOL_RESULT_MCP_AUTHENTICATE_REFRESH_REFUSED_VAR_1
-->
The sign-in server refused the last token refresh of MCP server "${TOOL_RESULT_MCP_AUTHENTICATE_REFRESH_REFUSED_VAR_0(TOOL_RESULT_MCP_AUTHENTICATE_REFRESH_REFUSED_VAR_1)}", perhaps only for a moment. Ask the user to run \`/mcp reconnect ${TOOL_RESULT_MCP_AUTHENTICATE_REFRESH_REFUSED_VAR_0(TOOL_RESULT_MCP_AUTHENTICATE_REFRESH_REFUSED_VAR_1)}\` or, if that doesn't help, \`/mcp\` to sign in again.
