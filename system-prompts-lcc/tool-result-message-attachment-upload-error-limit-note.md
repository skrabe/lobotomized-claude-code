<!--
name: 'Tool Result: Message attachment upload error limit note'
description: >-
  Attachment upload error explanation in the message delivery tool result,
  noting a suspected account upload limit and a size guaranteed to fit.
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_0
  - TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_1
  - TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_2
-->
${TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_0.upload_error} — either a passing fault, or the file is over this account's upload limit, which the server did not name; no account's limit is under ${TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_1(TOOL_RESULT_MESSAGE_ATTACHMENT_UPLOAD_ERROR_LIMIT_NOTE_VAR_2)}, so a copy under that size is sure to fit
