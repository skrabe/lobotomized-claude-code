<!--
name: Large-output read guidance (read all lines)
description: >-
  Tool-result guidance fragment to read all lines in chunks and summarize
  verbatim.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_READ_LARGE_FILE_CHUNK_ALL_VAR_0
  - TOOL_RESULT_READ_LARGE_FILE_CHUNK_ALL_VAR_1
  - TOOL_RESULT_READ_LARGE_FILE_CHUNK_ALL_VAR_2
-->
Read ${TOOL_RESULT_READ_LARGE_FILE_CHUNK_ALL_VAR_0} in chunks of ~${TOOL_RESULT_READ_LARGE_FILE_CHUNK_ALL_VAR_1} lines using offset/limit until you have read all ${TOOL_RESULT_READ_LARGE_FILE_CHUNK_ALL_VAR_2.count.toLocaleString()} lines, then summarize and quote any key findings verbatim.
