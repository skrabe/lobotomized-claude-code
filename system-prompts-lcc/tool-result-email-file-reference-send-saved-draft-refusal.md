<!--
name: 'Tool Result: Email file reference send saved draft refusal'
description: >-
  Refuses sending a saved draft named by draftId with files by reference since
  its recipients aren't shown
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_SEND_SAVED_DRAFT_REFUSAL_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_SEND_SAVED_DRAFT_REFUSAL_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_SEND_SAVED_DRAFT_REFUSAL_VAR_2
-->
This ${TOOL_RESULT_EMAIL_FILE_REFERENCE_SEND_SAVED_DRAFT_REFUSAL_VAR_0.toolName} call sends the saved draft that "draftId" names, and the call doesn't show that draft's recipients, so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_SEND_SAVED_DRAFT_REFUSAL_VAR_1}. Make a new draft with ${TOOL_RESULT_EMAIL_FILE_REFERENCE_SEND_SAVED_DRAFT_REFUSAL_VAR_2.toolName} that names the recipients and attaches the files, or send a new message without "draftId" that names its recipients in "to", "cc" or "bcc".
