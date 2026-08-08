<!--
name: 'Tool Result: memory_list entries wrapper'
description: >-
  Wrapper the memory_list tool result uses around the shared-store
  reference-data header, the listed document rows, and the 'call again with
  cursor' continuation note.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_0
  - TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_1
  - TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_2
  - TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_3
-->
${TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_0}

${TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_1.map(TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_2).join(`
`)}${TOOL_RESULT_MEMORY_LIST_ENTRIES_WRAPPER_VAR_3}
