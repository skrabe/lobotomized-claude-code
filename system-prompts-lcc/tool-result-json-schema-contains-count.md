<!--
name: 'Tool result: JSON schema contains count'
description: >-
  Ajv validation message for an array without enough (or with too many) items
  matching contains.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_JSON_SCHEMA_CONTAINS_COUNT_VAR_0
  - TOOL_RESULT_JSON_SCHEMA_CONTAINS_COUNT_VAR_1
-->
must contain at least ${TOOL_RESULT_JSON_SCHEMA_CONTAINS_COUNT_VAR_0}${TOOL_RESULT_JSON_SCHEMA_CONTAINS_COUNT_VAR_1===void 0?"":` and no more than ${TOOL_RESULT_JSON_SCHEMA_CONTAINS_COUNT_VAR_1}`} valid item(s)
