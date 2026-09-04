<!--
name: JSON Schema Enum Type Mismatch
description: Finding message when a schema's type does not match any of its enum values.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_JSON_SCHEMA_ENUM_TYPE_MISMATCH_VAR_0
  - TOOL_RESULT_JSON_SCHEMA_ENUM_TYPE_MISMATCH_VAR_1
  - TOOL_RESULT_JSON_SCHEMA_ENUM_TYPE_MISMATCH_VAR_2
-->
${TOOL_RESULT_JSON_SCHEMA_ENUM_TYPE_MISMATCH_VAR_0} declares type ${TOOL_RESULT_JSON_SCHEMA_ENUM_TYPE_MISMATCH_VAR_1(TOOL_RESULT_JSON_SCHEMA_ENUM_TYPE_MISMATCH_VAR_2)} but none of its enum values has that type, so no value can satisfy it — change type to match the enum values or vice versa
