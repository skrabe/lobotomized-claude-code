<!--
name: 'project_read: Binary Upload Saved Locally'
description: >-
  `notice` field of the object k5y() returns for a project_read of a non-text
  upload, telling the model the original bytes were written to local_file and to
  open them with file-appropriate tooling.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_0
  - TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_1
  - TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_2
-->

"${TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_0(TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_1)}" is a ${TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_0(TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_2.file_kind)} upload with no text extract; its original bytes (${TOOL_RESULT_PROJECT_READ_BINARY_UPLOAD_NOTICE_VAR_2.file_size_bytes}) were saved to local_file.
