<!--
name: 'Tool Result: Workflow script parse error with source excerpt'
description: >-
  Same parse-failure guidance but with the offending source line and a caret,
  giving the model the exact position to fix; it is the other branch of the same
  conditional as the no-location form.
ccVersion: 2.1.233
variables:
  - TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_WITH_SOURCE_EXCERPT_VAR_0
  - TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_WITH_SOURCE_EXCERPT_VAR_1
  - TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_WITH_SOURCE_EXCERPT_VAR_2
-->
Script parse error: ${TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_WITH_SOURCE_EXCERPT_VAR_0}

${TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_WITH_SOURCE_EXCERPT_VAR_1}
${TOOL_RESULT_WORKFLOW_SCRIPT_PARSE_ERROR_WITH_SOURCE_EXCERPT_VAR_2}

${"Workflow scripts must be plain JavaScript — common causes are TypeScript syntax (type annotations, interfaces, generics) and broken string quoting or escaping."}
