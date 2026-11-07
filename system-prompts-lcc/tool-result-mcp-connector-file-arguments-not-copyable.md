<!--
name: 'Tool Result: MCP connector arguments could not be copied'
description: >-
  Refuses a file call whose arguments could not be copied and asks for fewer or
  flatter arguments
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENTS_NOT_COPYABLE_VAR_0
-->
No file was sent: Claude Code could not make a copy of this call's arguments, so it did not ask. Arguments that hold very many values, or lists and objects nested very deeply, cannot be copied: make the call with fewer or flatter ones. If these are neither, this is a bug in Claude Code that the user cannot fix. ${TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENTS_NOT_COPYABLE_VAR_0}
