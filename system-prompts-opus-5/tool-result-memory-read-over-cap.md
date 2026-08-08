<!--
name: 'Tool Result: Memory document over read cap'
description: >-
  memory_read refusal returned to the model when the stored document exceeds the
  read cap, so its content is withheld.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_0
  - TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_1
  - TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_2
  - TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_3
-->
"${TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_0}" is ${TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_1.byteLength(TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_2.content,"utf8")} bytes, over the ${TOOL_RESULT_MEMORY_READ_OVER_CAP_VAR_3}-byte read cap, so its content is not returned.
