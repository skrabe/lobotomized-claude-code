<!--
name: 'Tool Result: Unknown Memory Store Id'
description: >-
  Refusal returned when the model passes a store id that is not available in this
  session; lists available ids and points at memory_list.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_0
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_1
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_2
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_3
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_4
-->
No memory store with id ${TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_0(TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_1)} is available in this session. Available stores: ${TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_2}.${TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_4}
