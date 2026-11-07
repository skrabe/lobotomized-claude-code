<!--
name: 'Tool Result: MCP connector raw call refused (arguments not copied)'
description: >-
  Refuses a raw connector call whose arguments could not be copied and asks for
  plain, flatter JSON values
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NOT_COPIED_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_RAW_CALL_NOT_COPIED_VAR_0} was not called: Claude Code could not copy this call's arguments, so it could not tell what the call would send. Calling again with the same arguments will not work: use plain JSON values, and fewer or flatter ones if they are very many or very deeply nested.
