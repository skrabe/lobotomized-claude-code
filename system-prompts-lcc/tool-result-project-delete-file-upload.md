<!--
name: 'Tool Result: project_delete cannot remove file upload'
description: project_delete error when the path is a file upload rather than a text doc.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_PROJECT_DELETE_FILE_UPLOAD_VAR_0
  - TOOL_RESULT_PROJECT_DELETE_FILE_UPLOAD_VAR_1
-->
"${TOOL_RESULT_PROJECT_DELETE_FILE_UPLOAD_VAR_0(TOOL_RESULT_PROJECT_DELETE_FILE_UPLOAD_VAR_1)}" is a file upload; project_delete only removes text docs. File uploads can be removed from the project in claude.ai.
