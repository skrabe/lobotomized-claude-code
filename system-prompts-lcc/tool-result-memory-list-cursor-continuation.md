<!--
name: 'Tool Result: Memory listing cursor continuation'
description: >-
  Trailer appended to a capped memory_list tool_result telling the model how
  many entries remain and which cursor to pass next.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_0
  - TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_1
  - TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_2
  - TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_3
-->

… ${TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_0} more — call again with cursor=${TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_1.stringify(TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_2.at(-1)?.TOOL_RESULT_MEMORY_LIST_CURSOR_CONTINUATION_VAR_3??"")} to continue.
