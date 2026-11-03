<!--
name: 'Tool Result: Email file reference file too large'
description: >-
  Says a referenced file exceeds the attachment limit, forbids base64 workaround
  and asks to tell the user
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_2
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_3
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_0} is over the ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_1.maxFileText} limit for attachments from here, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_2} Don't try to attach it another way, such as putting its base64 in the ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOO_LARGE_VAR_3} field. Tell the user the file is too large to attach from here.
