<!--
name: 'Tool result: MCP call failed after declined server question'
description: >-
  Error text returned for an MCP tool call that failed or was answered after the
  server's elicitation question was declined, telling the model the decline
  stands and a repeat call repeats the request.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_QUESTION_DECLINED_CALL_FAILED_VAR_0
-->
${TOOL_RESULT_MCP_QUESTION_DECLINED_CALL_FAILED_VAR_0===""?"This call failed. That":`The server replied: "${TOOL_RESULT_MCP_QUESTION_DECLINED_CALL_FAILED_VAR_0}". That reply`} came after a question that the server asked about this call was declined, and the decline still stands. Another call for this action repeats the request that the question was about.
