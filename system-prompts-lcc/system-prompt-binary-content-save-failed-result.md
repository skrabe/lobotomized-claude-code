<!--
name: 'System Prompt: Binary content save-failure result'
description: >-
  Tool_result text reporting that binary content (type, size) could not be saved
  to disk, with the error
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_0
  - SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_1
  - SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_2
  - SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_3
-->
${SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_0}Binary content (${SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_1||"unknown type"}, ${SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_2.length} bytes) could not be saved to disk: ${SYSTEM_PROMPT_BINARY_CONTENT_SAVE_FAILED_RESULT_VAR_3.error}
