<!--
name: 'Tool Result: MCP App views left out (answer too large)'
description: >-
  Tells the model which views were left out because the answer would be too
  large and how to fetch one by its view id
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_0
  - TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_1
  - TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_2
  - TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_3
  - TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_4
-->
${TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_0.length===1?"1 view was":`${TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_0.length} of the ${TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_1.length} views were`} left out because the answer would be too large; "${TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_2}" inside the tag above names ${TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_0.length===1?"it":TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_3(TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_0.length,TOOL_RESULT_MCP_APP_VIEWS_LEFT_OUT_TOO_LARGE_ANSWER_VAR_4)}. To get one, call again with its view id, where the tag shows one. 
