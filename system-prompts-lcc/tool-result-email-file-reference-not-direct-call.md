<!--
name: 'Tool Result: Email file reference not a direct call'
description: >-
  Refuses file references in a call made by an artifact or plugin code, asking
  for a direct call or base64
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_NOT_DIRECT_CALL_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_NOT_DIRECT_CALL_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_NOT_DIRECT_CALL_VAR_2
-->
Files can't be attached by reference in a ${TOOL_RESULT_EMAIL_FILE_REFERENCE_NOT_DIRECT_CALL_VAR_0.toolName} call made by an artifact or a plugin's own code, so nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_NOT_DIRECT_CALL_VAR_1}. Make the ${TOOL_RESULT_EMAIL_FILE_REFERENCE_NOT_DIRECT_CALL_VAR_0.toolName} call directly, or put each file's base64 in its attachment's ${TOOL_RESULT_EMAIL_FILE_REFERENCE_NOT_DIRECT_CALL_VAR_2} field.
