<!--
name: 'Tool Result: Read file too large'
description: >-
  Read tool error when a file's content exceeds the maximum readable size,
  telling the model to use offset/limit or search instead.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_0
  - TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_1
  - TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_2
  - TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_3
-->
File content (${TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_0(TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_1)}) exceeds maximum allowed size (${TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_0(TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_2)}). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.${TOOL_RESULT_READ_FILE_TOO_LARGE_VAR_3}
