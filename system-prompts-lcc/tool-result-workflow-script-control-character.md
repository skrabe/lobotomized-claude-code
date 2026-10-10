<!--
name: 'Tool result: workflow script control character'
description: >-
  Workflow validation error when the script contains a control character an
  approval prompt cannot show.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_WORKFLOW_SCRIPT_CONTROL_CHARACTER_VAR_0
-->
${TOOL_RESULT_WORKFLOW_SCRIPT_CONTROL_CHARACTER_VAR_0.scriptPath?`Workflow script file ${TOOL_RESULT_WORKFLOW_SCRIPT_CONTROL_CHARACTER_VAR_0.scriptPath}`:`The file of workflow "${TOOL_RESULT_WORKFLOW_SCRIPT_CONTROL_CHARACTER_VAR_0.name}"`} contains a control character that an approval prompt cannot show, such as an escape byte or a carriage return that is not part of a CRLF line ending. Remove it from the file and try again.
