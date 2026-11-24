<!--
name: 'Tool Result: Check MCP task, plain call without status'
description: >-
  Check MCP task result for a backgrounded plain MCP call whose server gives no
  status.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_CHECK_MCP_TASK_PLAIN_CALL_NO_STATUS_VAR_0
-->
Task ${TOOL_RESULT_CHECK_MCP_TASK_PLAIN_CALL_NO_STATUS_VAR_0} is an MCP tool call that is still running in the background. Its server gives no status for it. What the tool result that moved it to the background says about its result still holds. Tell the user, and do not check again unless they ask again.
