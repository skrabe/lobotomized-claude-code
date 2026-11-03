<!--
name: 'Tool Result: Email file reference invalid reply id'
description: >-
  Refuses attaching files when replyToMessageId isn't a Gmail message id and
  asks to retry with a valid id or none
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_REPLY_ID_INVALID_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_REPLY_ID_INVALID_VAR_1
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_REPLY_ID_INVALID_VAR_0}'s "replyToMessageId" isn't the Gmail id of a message (8 to 32 hexadecimal characters, not its Message-ID header), so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_REPLY_ID_INVALID_VAR_1}. Make the call again with the id of the message it answers, or without it to start a new email.
