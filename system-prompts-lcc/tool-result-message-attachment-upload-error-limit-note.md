<!--
name: 'Tool Result: Message attachment upload error limit note'
description: >-
  Attachment upload error explanation in the message delivery tool result,
  noting a suspected account upload limit and a size guaranteed to fit.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_0
  - TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_1
  - TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_2
-->
${TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_0.upload_error} — the cause is unknown and may pass. If the same file fails like this again, it may be over the upload limit that applies to this session, which was not named and is never under ${TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_1(TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_2)}
