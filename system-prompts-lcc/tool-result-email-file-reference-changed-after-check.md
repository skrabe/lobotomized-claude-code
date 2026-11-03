<!--
name: 'Tool Result: Email file reference changed after check'
description: >-
  Says a referenced file changed after it was checked so nothing was sent,
  asking to recompute its SHA-256 and retry
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_CHANGED_AFTER_CHECK_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_CHANGED_AFTER_CHECK_VAR_1
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_CHANGED_AFTER_CHECK_VAR_0} changed after it was checked, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_CHANGED_AFTER_CHECK_VAR_1} Compute its SHA-256 again and make the call again. If it changes again, tell the user.
