<!--
name: 'Tool result: Git bundle upload file too large'
description: Problem clause that a file is larger than the MiB limit that is copied
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_GIT_BUNDLE_UPLOAD_FILE_TOO_LARGE_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_UPLOAD_FILE_TOO_LARGE_VAR_1
-->
is larger than ${TOOL_RESULT_GIT_BUNDLE_UPLOAD_FILE_TOO_LARGE_VAR_0.floor(TOOL_RESULT_GIT_BUNDLE_UPLOAD_FILE_TOO_LARGE_VAR_1/1048576)} MiB, the most that is copied
