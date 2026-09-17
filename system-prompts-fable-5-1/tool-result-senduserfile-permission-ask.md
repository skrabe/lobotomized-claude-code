<!--
name: 'Tool Result: SendUserFile Permission Ask'
description: >-
  SendUserFile checkPermissions ask prompt to send N files, noting that
  SendUserFile reads file contents.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_SENDUSERFILE_PERMISSION_ASK_VAR_0
  - TOOL_RESULT_SENDUSERFILE_PERMISSION_ASK_VAR_1
-->
Send ${TOOL_RESULT_SENDUSERFILE_PERMISSION_ASK_VAR_0.files.length} ${TOOL_RESULT_SENDUSERFILE_PERMISSION_ASK_VAR_1(TOOL_RESULT_SENDUSERFILE_PERMISSION_ASK_VAR_0.files.length,"file")} to the user? SendUserFile reads file contents.
