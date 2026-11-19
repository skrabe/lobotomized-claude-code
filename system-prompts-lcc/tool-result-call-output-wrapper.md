<!--
name: 'Tool Result: Call output wrapper'
description: Wraps an attached tool call's output as 'Result of calling the tool'
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_0
  - TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_1
  - TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_2
-->
Result of calling the ${TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_0.name} tool:
${TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_1(TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_2)}
