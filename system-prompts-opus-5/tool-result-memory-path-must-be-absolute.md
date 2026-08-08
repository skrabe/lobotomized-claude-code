<!--
name: 'Tool Result: Memory path must be absolute'
description: >-
  Refusal returned when the model passes a relative memory path, suggesting the
  absolute form and the store's root prefix.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_PATH_MUST_BE_ABSOLUTE_VAR_0
  - TOOL_RESULT_MEMORY_PATH_MUST_BE_ABSOLUTE_VAR_1
  - TOOL_RESULT_MEMORY_PATH_MUST_BE_ABSOLUTE_VAR_2
-->
Memory paths are absolute and start with "/" — use ${TOOL_RESULT_MEMORY_PATH_MUST_BE_ABSOLUTE_VAR_0(TOOL_RESULT_MEMORY_PATH_MUST_BE_ABSOLUTE_VAR_1)}. This store's memories live under /${TOOL_RESULT_MEMORY_PATH_MUST_BE_ABSOLUTE_VAR_2}.
