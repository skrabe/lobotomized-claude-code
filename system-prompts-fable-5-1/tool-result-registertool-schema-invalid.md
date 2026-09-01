<!--
name: registerTool schema invalid
description: >-
  REPL registerTool error surfaced to the model when the schema is not a
  JSON-serializable object.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_REGISTERTOOL_SCHEMA_INVALID_VAR_0
  - TOOL_RESULT_REGISTERTOOL_SCHEMA_INVALID_VAR_1
-->
registerTool: schema must be a JSON-serializable object, got ${TOOL_RESULT_REGISTERTOOL_SCHEMA_INVALID_VAR_0===null?"null":TOOL_RESULT_REGISTERTOOL_SCHEMA_INVALID_VAR_1.isArray(TOOL_RESULT_REGISTERTOOL_SCHEMA_INVALID_VAR_0)?"array":typeof TOOL_RESULT_REGISTERTOOL_SCHEMA_INVALID_VAR_0}
