<!--
name: 'Tool Result: Email file reference argument not text'
description: >-
  Refuses attaching files when an email argument isn't text and asks to pass it
  as a string or omit it
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_2
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_3
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_0}'s ${TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_1(TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_2)} isn't text, so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_ARGUMENT_NOT_TEXT_VAR_3}. Make the call again with it as a string, or without it.
