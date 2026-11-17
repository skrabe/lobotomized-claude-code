<!--
name: 'Tool Result: Attachment is a special file'
description: Refuses an attachment path that is a links-type or device/process file
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_ATTACHMENT_SPECIAL_FILE_KIND_VAR_0
  - TOOL_RESULT_ATTACHMENT_SPECIAL_FILE_KIND_VAR_1
  - TOOL_RESULT_ATTACHMENT_SPECIAL_FILE_KIND_VAR_2
-->
Attachment "${TOOL_RESULT_ATTACHMENT_SPECIAL_FILE_KIND_VAR_0}" is ${TOOL_RESULT_ATTACHMENT_SPECIAL_FILE_KIND_VAR_1==="links"?TOOL_RESULT_ATTACHMENT_SPECIAL_FILE_KIND_VAR_2:"a device or process file, which this tool does not send"}.
