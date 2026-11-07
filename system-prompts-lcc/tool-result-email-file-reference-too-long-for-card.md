<!--
name: 'Tool Result: Email file reference call too long'
description: >-
  Refuses an email call attaching files by reference that exceeds 150,000
  characters, asking for a shorter message or base64 content
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_1
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_0} is over the 150,000 characters a call that attaches files by reference may come to, so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_1}. Make the call again with a shorter message and any long text or typed attachment in a file attached by reference, or with each file's base64 in its attachment's "content".
