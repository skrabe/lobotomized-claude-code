<!--
name: Tool result output wrapper
description: >-
  Meta message wrapping a tool's output as 'Result of calling the X tool: …',
  injected into the model's context.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_0
  - TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_1
-->
Result of calling the ${TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_0.name} tool:
${TOOL_RESULT_CALL_OUTPUT_WRAPPER_VAR_1}
