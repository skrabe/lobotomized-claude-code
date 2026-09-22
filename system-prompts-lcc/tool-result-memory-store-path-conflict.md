<!--
name: 'Tool Result: Memory document path conflict'
description: >-
  memory_write failure returned to the model when the requested path collides
  with an existing document or one of its ancestors.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_STORE_PATH_CONFLICT_VAR_0
  - TOOL_RESULT_MEMORY_STORE_PATH_CONFLICT_VAR_1
-->
"${TOOL_RESULT_MEMORY_STORE_PATH_CONFLICT_VAR_0}" cannot be created: ${TOOL_RESULT_MEMORY_STORE_PATH_CONFLICT_VAR_1}. A document and a prefix of its path cannot coexist — choose a different path.
