<!--
name: 'Tool Result: tool.run step output shape mismatch'
description: >-
  Error when a plugin tool.run step resolved the tool with a result that does
  not match its output schema
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_TOOL_RUN_STEP_OUTPUT_SHAPE_MISMATCH_VAR_0
  - TOOL_RESULT_TOOL_RUN_STEP_OUTPUT_SHAPE_MISMATCH_VAR_1
-->
tool.run step resolved ${TOOL_RESULT_TOOL_RUN_STEP_OUTPUT_SHAPE_MISMATCH_VAR_0.name} with a result that does not match its output shape: ${TOOL_RESULT_TOOL_RUN_STEP_OUTPUT_SHAPE_MISMATCH_VAR_1.error.message}
