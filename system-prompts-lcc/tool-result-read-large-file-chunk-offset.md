<!--
name: Large-output read guidance (chunk offset/limit)
description: Tool-result guidance fragment to read the file in chunks via offset/limit.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_READ_LARGE_FILE_CHUNK_OFFSET_VAR_0
  - TOOL_RESULT_READ_LARGE_FILE_CHUNK_OFFSET_VAR_1
-->
read ${TOOL_RESULT_READ_LARGE_FILE_CHUNK_OFFSET_VAR_0} in chunks of ~${TOOL_RESULT_READ_LARGE_FILE_CHUNK_OFFSET_VAR_1} lines using offset/limit until you have read 100% of it.
