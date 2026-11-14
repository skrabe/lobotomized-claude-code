<!--
name: 'Tool Result: Input not valid JSON, retry'
description: >-
  Tool-use error telling the model its tool input could not be parsed as JSON,
  listing common causes and asking it to retry with valid JSON.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_0
  - TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_1
-->
${TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_0} was called with input that could not be parsed as JSON.
${TOOL_RESULT_INPUT_NOT_VALID_JSON_RETRY_VAR_1}Common causes: unescaped backslashes in file paths (use / or \\\\), unescaped control characters, or truncated output. Retry with valid JSON.
