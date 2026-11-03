<!--
name: 'Tool Result: Email file reference total too large'
description: >-
  Says the referenced files together exceed the per-email limit, forbids
  attaching another way and asks the user what to do
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOTAL_TOO_LARGE_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOTAL_TOO_LARGE_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_TOTAL_TOO_LARGE_VAR_2
-->
The files this call attaches by reference come to more than ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOTAL_TOO_LARGE_VAR_0.maxTotalText??""} together, over the limit for attachments sent in one email from here, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOTAL_TOO_LARGE_VAR_1} Don't try to attach them another way, such as putting their base64 in the ${TOOL_RESULT_EMAIL_FILE_REFERENCE_TOTAL_TOO_LARGE_VAR_2} fields. Tell the user the files are too large to send in one email, and ask what they'd like to do.
