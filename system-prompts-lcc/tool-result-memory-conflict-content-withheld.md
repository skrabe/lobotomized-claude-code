<!--
name: 'Tool Result: Memory conflict with oversized content withheld'
description: >-
  Clause appended to a memory_write conflict tool_result when the current
  document is over the read cap, telling the model to replace it wholesale or
  leave it.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_0
  - TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_1
  - TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_2
  - TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_3
-->
 Its current content is ${TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_0} bytes, over the ${TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_1}-byte read cap, so it is withheld here and ${TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_2} refuses it for the same reason; replace the document wholesale with if_version=${TOOL_RESULT_MEMORY_CONFLICT_CONTENT_WITHHELD_VAR_3}, or leave it as is.
