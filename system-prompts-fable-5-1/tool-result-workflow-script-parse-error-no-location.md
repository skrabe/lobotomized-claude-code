<!--
name: 'Tool Result: Workflow script parse error (no source location)'
description: >-
  Reports the parse failure and names the likely causes (TypeScript syntax,
  broken quoting/escaping) so the model knows what to change; this branch fires
  when the parser gave no line/column.
ccVersion: 2.1.233
variables:
  - TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_NO_LOCATION_VAR_0
-->
Script parse error: ${TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_NO_LOCATION_VAR_0}. ${"Workflow scripts must be plain JavaScript — common causes are TypeScript syntax (type annotations, interfaces, generics) and broken string quoting or escaping."}
