<!--
name: 'Tool Result: Write path is directory'
description: >-
  Write validation error when file_path is a directory, telling the model to
  include the file name
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_PATH_IS_DIRECTORY_VAR_0
  - TOOL_RESULT_WRITE_PATH_IS_DIRECTORY_VAR_1
-->
${TOOL_RESULT_WRITE_PATH_IS_DIRECTORY_VAR_0(TOOL_RESULT_WRITE_PATH_IS_DIRECTORY_VAR_1)} is a directory, not a file. To create a file inside it, include the file name in file_path.
