<!--
name: 'Tool Result: File reference upload approval ask'
description: >-
  checkPermissions ask message when Claude wants to upload a file by reference
  to a connector service, which needs approval even if the tool is already
  allowed; on decline it is the tool_result.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_FILE_REFERENCE_UPLOAD_APPROVAL_ASK_VAR_0
-->
Claude wants to upload a file to ${TOOL_RESULT_FILE_REFERENCE_UPLOAD_APPROVAL_ASK_VAR_0.row.serviceName}. This upload needs your approval even if you already allowed this tool.
