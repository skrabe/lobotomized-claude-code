<!--
name: JSON Schema Required Property Forbidden
description: >-
  Finding message when required lists a property that is not in properties while
  additionalProperties is false.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_JSON_SCHEMA_REQUIRED_PROPERTY_FORBIDDEN_VAR_0
  - TOOL_RESULT_JSON_SCHEMA_REQUIRED_PROPERTY_FORBIDDEN_VAR_1
  - TOOL_RESULT_JSON_SCHEMA_REQUIRED_PROPERTY_FORBIDDEN_VAR_2
-->
${TOOL_RESULT_JSON_SCHEMA_REQUIRED_PROPERTY_FORBIDDEN_VAR_0} lists "${TOOL_RESULT_JSON_SCHEMA_REQUIRED_PROPERTY_FORBIDDEN_VAR_1(TOOL_RESULT_JSON_SCHEMA_REQUIRED_PROPERTY_FORBIDDEN_VAR_2)}" in required but does not declare it in properties, and additionalProperties is false, so no object can satisfy it — declare the property or drop it from required
