<!--
name: 'Tool Result: Email file reference too many attachments'
description: >-
  Refuses attaching files by reference when the email has more than the
  attachment limit and asks to split the send
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_MANY_ATTACHMENTS_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_MANY_ATTACHMENTS_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_MANY_ATTACHMENTS_VAR_2
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_MANY_ATTACHMENTS_VAR_0} carries more than ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_MANY_ATTACHMENTS_VAR_1.maxAttachments??0} attachments, so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_MANY_ATTACHMENTS_VAR_2}. Make the call again with at most ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_MANY_ATTACHMENTS_VAR_1.maxAttachments??0} attachments, and send the others in another email.
