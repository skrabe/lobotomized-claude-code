<!--
name: 'Tool Result: Memory write stale version'
description: >-
  memory_write conflict lead returned to the model when the document changed
  since it was read and the supplied if_version is stale.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_WRITE_STALE_VERSION_VAR_0
  - TOOL_RESULT_MEMORY_WRITE_STALE_VERSION_VAR_1
  - TOOL_RESULT_MEMORY_WRITE_STALE_VERSION_VAR_2
-->
"${TOOL_RESULT_MEMORY_WRITE_STALE_VERSION_VAR_0}" changed since you last read it (if_version ${TOOL_RESULT_MEMORY_WRITE_STALE_VERSION_VAR_1} is stale; current version ${TOOL_RESULT_MEMORY_WRITE_STALE_VERSION_VAR_2}).
