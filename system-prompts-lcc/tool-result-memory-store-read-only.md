<!--
name: 'Tool Result: Memory store is read-only'
description: >-
  Refusal returned on a memory_write to a read-only store, naming the writable
  stores instead.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_STORE_READ_ONLY_VAR_0
  - TOOL_RESULT_MEMORY_STORE_READ_ONLY_VAR_1
  - TOOL_RESULT_MEMORY_STORE_READ_ONLY_VAR_2
-->
The memory store ${TOOL_RESULT_MEMORY_STORE_READ_ONLY_VAR_0(TOOL_RESULT_MEMORY_STORE_READ_ONLY_VAR_1)} is read-only in this session; changes will not persist.${TOOL_RESULT_MEMORY_STORE_READ_ONLY_VAR_2}
