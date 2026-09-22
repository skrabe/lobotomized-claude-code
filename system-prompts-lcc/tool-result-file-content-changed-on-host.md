<!--
name: 'Tool Result: File Content Changed On Host'
description: >-
  Edit/Write tool_result when a remote-host file's content no longer matches
  this session's read baseline; retry after Read with _host.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_FILE_CONTENT_CHANGED_ON_HOST_VAR_0
-->
File content on ${TOOL_RESULT_FILE_CONTENT_CHANGED_ON_HOST_VAR_0} has changed since this session read it. Read it again there (Read with "_host": "${TOOL_RESULT_FILE_CONTENT_CHANGED_ON_HOST_VAR_0}"), then retry.
