<!--
name: 'Tool Result: Write path not regular file'
description: >-
  Write validation error when the path exists but is a device, FIFO or socket
  rather than a regular file
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_PATH_NOT_REGULAR_FILE_VAR_0
  - TOOL_RESULT_WRITE_PATH_NOT_REGULAR_FILE_VAR_1
-->
${TOOL_RESULT_WRITE_PATH_NOT_REGULAR_FILE_VAR_0(TOOL_RESULT_WRITE_PATH_NOT_REGULAR_FILE_VAR_1)} exists but is not a regular file (a device, FIFO or socket). Write only creates or overwrites regular files.
