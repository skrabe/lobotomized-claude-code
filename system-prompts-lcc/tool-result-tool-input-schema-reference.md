<!--
name: Tool input schema reference
description: >-
  Appended to a tool input-validation tool_use_error result, giving the model
  the undiscovered tool’s input schema for reference.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_0
  - TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_1
  - TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_2
-->
 For reference, this tool's input schema is: ${TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_0(TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_1(TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_2.inputSchema))}
