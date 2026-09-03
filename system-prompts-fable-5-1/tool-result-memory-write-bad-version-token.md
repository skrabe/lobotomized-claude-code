<!--
name: 'Tool Result: Memory write malformed if_version'
description: >-
  memory_write conflict lead returned to the model when if_version is neither a
  12-character version token nor the literal word new.
ccVersion: 2.1.224
variables:
  - TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_0
  - TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_1
  - TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_2
  - TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_3
-->
if_version "${TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_0(TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_1)}" is not a version token — pass the 12-character token from your most recent ${TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_2} or ${TOOL_RESULT_MEMORY_WRITE_BAD_VERSION_TOKEN_VAR_3} of this path, or the literal word new for a document that does not yet exist.
