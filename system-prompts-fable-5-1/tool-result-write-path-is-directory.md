<!--
name: 'Tool Result: Write Path Is A Directory'
description: >-
  Write validateInput error returned to the model when file_path names an
  existing directory, telling it to include the file name.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_WRITE_PATH_IS_DIRECTORY_VAR_0
-->
${TOOL_RESULT_WRITE_PATH_IS_DIRECTORY_VAR_0} is a directory, not a file. To create a file inside it, include the file name in file_path.
