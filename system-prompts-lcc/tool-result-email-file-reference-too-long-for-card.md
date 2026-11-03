<!--
name: 'Tool Result: Email file reference too long for approval card'
description: >-
  Refuses attaching files by reference when the email is too long for the
  approval card to show recipients and files
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_1
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_0} is too long for the approval card to show who gets which files, so files can't be attached to it by reference and nothing was sent to ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LONG_FOR_CARD_VAR_1}. Make the call again with a shorter message and any long text or typed attachment in a file attached by reference, or with fewer recipients or files or shorter file paths, or with each file's base64 in its attachment's "content", and send the rest in another email.
