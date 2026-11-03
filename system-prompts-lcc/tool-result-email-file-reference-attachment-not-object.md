<!--
name: 'Tool Result: Email file reference attachment not object'
description: Refuses an attachment that isn't an object and shows the expected object shape
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_NOT_OBJECT_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_NOT_OBJECT_VAR_1
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_NOT_OBJECT_VAR_0} in this call isn't an object, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_NOT_OBJECT_VAR_1} Make the call again with each attachment an object, such as {"content": "...", "filename": "report.pdf"}.
