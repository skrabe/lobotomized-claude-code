<!--
name: 'Tool result: MCP server input request unservable'
description: >-
  Tells the model a named MCP server asked for input this client could not
  serve, with the method, so the call was not made again
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_SERVER_INPUT_REQUEST_UNSERVABLE_VAR_0
  - TOOL_RESULT_MCP_SERVER_INPUT_REQUEST_UNSERVABLE_VAR_1
-->
MCP server "${TOOL_RESULT_MCP_SERVER_INPUT_REQUEST_UNSERVABLE_VAR_0}" asked for input this client could not serve${TOOL_RESULT_MCP_SERVER_INPUT_REQUEST_UNSERVABLE_VAR_1===void 0?"":` (${TOOL_RESULT_MCP_SERVER_INPUT_REQUEST_UNSERVABLE_VAR_1})`}, so the call was not made again
