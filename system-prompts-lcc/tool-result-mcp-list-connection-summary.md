<!--
name: MCP server connection summary
description: >-
  Reports how many MCP servers connected, whether listing was cut, and whether
  tasks are relayed.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_0
  - TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_1
  - TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_2
  - TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_3
-->
${TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_0.size} of ${TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_1.length} servers connected${TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_2?", cut at a limit":""}${TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_3?", tasks relayed":""}
