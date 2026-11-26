<!--
name: PreToolUse mcp_tool hook could not run — refusing the gate
description: >-
  Built when a PreToolUse mcp_tool device hook is withheld/could not run for a
  served call; the text becomes blockingError.blockingError in the yielded
  result, the same channel that surfaces hook_blocking_error content to the
  model.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_PRETOOLUSE_MCP_HOOK_COULD_NOT_RUN_VAR_0
  - TOOL_RESULT_PRETOOLUSE_MCP_HOOK_COULD_NOT_RUN_VAR_1
-->
a ${TOOL_RESULT_PRETOOLUSE_MCP_HOOK_COULD_NOT_RUN_VAR_0} mcp_tool hook could not run (${TOOL_RESULT_PRETOOLUSE_MCP_HOOK_COULD_NOT_RUN_VAR_1.error}); refusing rather than skipping that gate
