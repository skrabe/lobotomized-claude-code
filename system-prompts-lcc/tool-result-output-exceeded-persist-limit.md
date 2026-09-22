<!--
name: 'Tool Result: Output Exceeded Persist Limit'
description: >-
  Persisted-output tool_result prefix when only the first truncatedAtBytes of a
  large result were saved to disk.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_OUTPUT_EXCEEDED_PERSIST_LIMIT_VAR_0
  - TOOL_RESULT_OUTPUT_EXCEEDED_PERSIST_LIMIT_VAR_1
-->
Output exceeded the ${TOOL_RESULT_OUTPUT_EXCEEDED_PERSIST_LIMIT_VAR_0(TOOL_RESULT_OUTPUT_EXCEEDED_PERSIST_LIMIT_VAR_1.truncatedAtBytes)} persist limit; only the first ${TOOL_RESULT_OUTPUT_EXCEEDED_PERSIST_LIMIT_VAR_0(TOOL_RESULT_OUTPUT_EXCEEDED_PERSIST_LIMIT_VAR_1.truncatedAtBytes)} were saved to: ${TOOL_RESULT_OUTPUT_EXCEEDED_PERSIST_LIMIT_VAR_1.filepath}

