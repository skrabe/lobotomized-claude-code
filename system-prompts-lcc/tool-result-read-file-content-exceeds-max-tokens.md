<!--
name: 'Tool Result: Read file content exceeds max tokens'
description: >-
  Error returned by the Read tool when a file's token count exceeds the maximum,
  advising offset/limit or search.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_READ_FILE_CONTENT_EXCEEDS_MAX_TOKENS_VAR_0
  - TOOL_RESULT_READ_FILE_CONTENT_EXCEEDS_MAX_TOKENS_VAR_1
-->
File content (${TOOL_RESULT_READ_FILE_CONTENT_EXCEEDS_MAX_TOKENS_VAR_0} tokens) exceeds maximum allowed tokens (${TOOL_RESULT_READ_FILE_CONTENT_EXCEEDS_MAX_TOKENS_VAR_1}). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
