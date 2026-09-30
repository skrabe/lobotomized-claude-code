<!--
name: 'project_read: Binary Upload Over Session File Limit'
description: >-
  `notice` field of the project_read result when a non-text upload's bytes
  exceed the session's per-file maxBytes, so nothing was saved and the model is
  told to say the file cannot be opened here.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_OVER_SESSION_FILE_LIMIT_VAR_0
  - TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_OVER_SESSION_FILE_LIMIT_VAR_1
-->
${TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_OVER_SESSION_FILE_LIMIT_VAR_0}are more than this session keeps in one file (${TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_OVER_SESSION_FILE_LIMIT_VAR_1.maxBytes} bytes), so they were not saved; tell the user this file cannot be opened here.
