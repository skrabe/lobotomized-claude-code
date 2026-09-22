<!--
name: 'Tool Result: Invalid memory path'
description: >-
  Refusal returned when a memory path fails validation, spelling out the length,
  segment, extension and character rules for the model.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_INVALID_PATH_VAR_0
  - TOOL_RESULT_MEMORY_INVALID_PATH_VAR_1
  - TOOL_RESULT_MEMORY_INVALID_PATH_VAR_2
-->
${TOOL_RESULT_MEMORY_INVALID_PATH_VAR_0(TOOL_RESULT_MEMORY_INVALID_PATH_VAR_1)} is not a valid memory path: use at most 1024 bytes, folder segments that do not start with "."${TOOL_RESULT_MEMORY_INVALID_PATH_VAR_2}, a filename ending in .md, .txt, .json, or .jsonl, and no control characters or backslashes.
