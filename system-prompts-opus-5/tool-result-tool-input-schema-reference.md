<!--
name: 'Tool Result: Undiscovered tool input-schema reference'
description: >-
  Reworded successor of the dropped tool-result-tool-input-schema-reference: the
  trailing sentence of the "schema was not sent to the API" tool_use_error that
  inlines the tool's JSON input schema so the model can retry. Id reused to
  preserve the user override.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_0
  - TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_1
  - TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_2
-->
 For reference, this tool's input schema is: ${TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_0(TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_1(TOOL_RESULT_TOOL_INPUT_SCHEMA_REFERENCE_VAR_2.inputSchema))}
