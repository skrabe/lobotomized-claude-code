<!--
name: 'Tool Result: File Modified On Host'
description: >-
  Host-aware Edit/Write stale-read error telling the model to re-Read with _host
  before writing a file that changed on that host.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_FILE_MODIFIED_ON_HOST_VAR_0
-->
File has been modified on ${TOOL_RESULT_FILE_MODIFIED_ON_HOST_VAR_0} since this session read it. Read it again there (Read with "_host": "${TOOL_RESULT_FILE_MODIFIED_ON_HOST_VAR_0}") before attempting to write it.
