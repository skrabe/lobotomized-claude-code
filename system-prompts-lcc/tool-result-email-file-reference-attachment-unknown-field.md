<!--
name: 'Tool Result: Email file reference attachment unknown field'
description: >-
  Refuses an attachment carrying a field it can't have and lists the allowed
  fields
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_0
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_1
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_2
  - TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_3
-->
${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_0} carries a field, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_1(TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_2)}, that an attachment can't have here, ${TOOL_RESULT_EMAIL_FILE_REFERENCE_ATTACHMENT_UNKNOWN_FIELD_VAR_3} Make the call again with no fields in an attachment but "content", "filename", "mimeType" and "inline".
