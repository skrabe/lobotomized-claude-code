<!--
name: 'Tool Result: Unknown memory store id'
description: >-
  Refusal returned when the model passes a store id that is not connected; lists
  the connected ids and points at memory_list.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_0
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_1
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_2
  - TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_3
-->
No memory store with id ${TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_0(TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_1)} is connected to this session. Connected stores: ${TOOL_RESULT_MEMORY_UNKNOWN_STORE_VAR_2}.
