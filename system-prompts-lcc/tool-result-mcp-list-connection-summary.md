<!--
name: MCP server connection summary
description: Reports how many MCP servers connected and whether listing was cut.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_0
  - TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_1
  - TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_2
-->
${TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_0.size} of ${TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_1.length} servers connected${TOOL_RESULT_MCP_LIST_CONNECTION_SUMMARY_VAR_2?", cut at a limit":""}
