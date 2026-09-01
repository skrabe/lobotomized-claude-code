<!--
name: 'Tool Result: Tool input not valid JSON, retry'
description: >-
  Tool-result error returned to the model when a tool call's input couldn't be
  parsed as JSON, showing the first bytes sent and common causes, asking it to
  retry with valid JSON.
ccVersion: 2.1.181
variables:
  - TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_0
  - TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_1
  - TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_2
-->
${TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_0.name} was called with input that could not be parsed as JSON.
You sent (first ${TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_1.length} of ${TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_2} bytes): ${TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_1}
Common causes: unescaped backslashes in file paths (use / or \\\\), unescaped control characters, or truncated output. Retry with valid JSON.
