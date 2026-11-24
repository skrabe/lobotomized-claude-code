<!--
name: MCP task backgrounded for subagent
description: >-
  Tool result for a subagent saying an MCP server-side task runs in the
  background and its result goes to the main conversation.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_0
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_1
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_2
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_3
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_4
  - TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_5
-->
MCP tool "${TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_0(TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_1,TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_2)}" started server-side task ${TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_3}, which runs on as background task ${TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_4}. Its result goes to the main conversation, not to you, so do not wait for it and do not repeat this call. Do what you can without it. In your report, say that task ${TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_4} is still running, that its result goes to the main conversation, and what the result is needed for.${TOOL_RESULT_MCP_TASK_BACKGROUNDED_FOR_SUBAGENT_VAR_5?" Say also that the result may not arrive until the user sends another message.":""}
