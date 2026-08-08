<!--
name: 'Tool Result: Connected memory stores listing'
description: >-
  memory_list tool_result header and per-store rows returned to the model when
  called with no arguments.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_0
  - TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_1
-->
${TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_0.stores.map((TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_1)=>`${TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_1.id}  (${TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_1.description}, ${TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_1.writable?"writable":"read-only"}, index ${TOOL_RESULT_MEMORY_LIST_CONNECTED_STORES_VAR_1.index})`).join(`
`)}
