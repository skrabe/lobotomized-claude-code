<!--
name: 'Tool result: notebook is not valid JSON'
description: Read tool error when a notebook file cannot be parsed as JSON
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_0
  - TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_1
  - TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_2
-->
Notebook file is not valid JSON (it may be truncated, corrupted, or still being written): ${TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_0 instanceof TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_1?TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_0.message:TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_2(TOOL_RESULT_NOTEBOOK_READ_INVALID_JSON_VAR_0)}
