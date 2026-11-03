<!--
name: 'Tool Result: Email file reference saved draft update refusal'
description: >-
  Refuses attaching files to a saved draft named by draftId whose recipients
  aren't shown, asking for a new draft naming all recipients
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_SAVED_DRAFT_UPDATE_REFUSAL_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_SAVED_DRAFT_UPDATE_REFUSAL_VAR_1
-->
This ${TOOL_RESULT_EMAIL_FILE_REFERENCE_SAVED_DRAFT_UPDATE_REFUSAL_VAR_0.toolName} call names a saved draft in "draftId", and the call doesn't show that draft's recipients, so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_SAVED_DRAFT_UPDATE_REFUSAL_VAR_1}. The saved draft wasn't changed. To attach the files, make a new draft: make the call again without "draftId", naming all of its recipients in "to", "cc" or "bcc".
