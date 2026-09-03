<!--
name: 'Tool Result: memory_write path missing'
description: >-
  Error returned to the model when memory_write targets a path that does not
  exist in the store and if_version was not set to new.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_WRITE_PATH_MISSING_VAR_0
  - TOOL_RESULT_MEMORY_WRITE_PATH_MISSING_VAR_1
-->
${TOOL_RESULT_MEMORY_WRITE_PATH_MISSING_VAR_0} failed: "${TOOL_RESULT_MEMORY_WRITE_PATH_MISSING_VAR_1.path}" does not exist in the memory store. Pass if_version=new to create it.
