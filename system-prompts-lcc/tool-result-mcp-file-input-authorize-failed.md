<!--
name: 'Tool result: MCP file input authorize failed'
description: >-
  Error for an MCP tool call when the server's file authorization request
  failed.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_MCP_FILE_INPUT_AUTHORIZE_FAILED_VAR_0
  - TOOL_RESULT_MCP_FILE_INPUT_AUTHORIZE_FAILED_VAR_1
-->
The files could not be attached${TOOL_RESULT_MCP_FILE_INPUT_AUTHORIZE_FAILED_VAR_0===""?".":`: ${TOOL_RESULT_MCP_FILE_INPUT_AUTHORIZE_FAILED_VAR_0}${/[.!?…]$/.test(TOOL_RESULT_MCP_FILE_INPUT_AUTHORIZE_FAILED_VAR_0)?"":"."}`} ${TOOL_RESULT_MCP_FILE_INPUT_AUTHORIZE_FAILED_VAR_1.nothingDone}
