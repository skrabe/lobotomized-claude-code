<!--
name: 'Tool Result: if_version=new but document exists'
description: >-
  memory_write conflict lead returned to the model when it passed if_version=new
  for a path that already exists.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_WRITE_IF_VERSION_NEW_EXISTS_VAR_0
  - TOOL_RESULT_MEMORY_WRITE_IF_VERSION_NEW_EXISTS_VAR_1
-->
if_version=new but "${TOOL_RESULT_MEMORY_WRITE_IF_VERSION_NEW_EXISTS_VAR_0}" already exists in the memory store (current version ${TOOL_RESULT_MEMORY_WRITE_IF_VERSION_NEW_EXISTS_VAR_1}).
