<!--
name: 'Tool Result: File input refused after unapplied same-response edit'
description: >-
  Validation error returned when a file-input tool call names a file whose Edit
  or Write earlier in the same response did not apply, so no file was sent.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_FILE_INPUT_SAME_RESPONSE_EDIT_NOT_APPLIED_VAR_0
  - TOOL_RESULT_FILE_INPUT_SAME_RESPONSE_EDIT_NOT_APPLIED_VAR_1
-->
The Edit or Write of ${TOOL_RESULT_FILE_INPUT_SAME_RESPONSE_EDIT_NOT_APPLIED_VAR_0} sent earlier in the same response did not apply (its own result says why), so no file was sent. Settle that change first (correct it, or leave the file as it is if the change was declined), then call ${TOOL_RESULT_FILE_INPUT_SAME_RESPONSE_EDIT_NOT_APPLIED_VAR_1.tool} again. ${TOOL_RESULT_FILE_INPUT_SAME_RESPONSE_EDIT_NOT_APPLIED_VAR_1.nothingDone}
