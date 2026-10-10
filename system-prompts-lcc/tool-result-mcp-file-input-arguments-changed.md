<!--
name: 'Tool result: MCP file input arguments changed'
description: >-
  Error for an MCP tool call whose arguments changed while waiting for approval;
  tells the model to call the tool again giving each file by its local field.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_MCP_FILE_INPUT_ARGUMENTS_CHANGED_VAR_0
-->
The arguments of this call changed while it waited for approval. Call ${TOOL_RESULT_MCP_FILE_INPUT_ARGUMENTS_CHANGED_VAR_0.tool} again, giving each file by its "${TOOL_RESULT_MCP_FILE_INPUT_ARGUMENTS_CHANGED_VAR_0.local}". ${TOOL_RESULT_MCP_FILE_INPUT_ARGUMENTS_CHANGED_VAR_0.nothingDone}
