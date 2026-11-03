<!--
name: 'Tool Result: Email file reference draft reply refusal'
description: >-
  Refuses attaching files to a draft reply via replyToMessageId and suggests a
  new draft or send_message
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_REPLY_REFUSAL_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_REPLY_REFUSAL_VAR_1
-->
This ${TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_REPLY_REFUSAL_VAR_0.toolName} call names a message to answer in "replyToMessageId", and who a reply saved as a draft reaches when it's sent hasn't been checked, so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_DRAFT_REPLY_REFUSAL_VAR_1}. Make the call again without "replyToMessageId", which saves a new draft outside the thread. If the person wants the reply sent now, use send_message.
