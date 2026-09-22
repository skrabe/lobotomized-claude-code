<!--
name: 'Tool Result: Tool call output does not match schema'
description: >-
  Error tool_result when a hooks-module tool.call result or a rewritten
  PostToolUse output fails the tool's output schema.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_TOOL_CALL_OUTPUT_SHAPE_MISMATCH_VAR_0
  - TOOL_RESULT_TOOL_CALL_OUTPUT_SHAPE_MISMATCH_VAR_1
-->
${TOOL_RESULT_TOOL_CALL_OUTPUT_SHAPE_MISMATCH_VAR_0.rewritten?"a managed PostToolUse hook rewrote":"tool.call step resolved"} ${TOOL_RESULT_TOOL_CALL_OUTPUT_SHAPE_MISMATCH_VAR_1.name} with a result that does not match its output shape: 
