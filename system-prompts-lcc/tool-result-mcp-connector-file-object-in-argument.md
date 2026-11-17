<!--
name: 'Tool Result: MCP connector file object written in argument'
description: >-
  Refuses a connector call whose argument holds a file object (id, mimeType,
  size), says no file is sent that way and not to retry with one
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_2
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_0} was not called: the argument ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_1} holds an object with an id, a mimeType and a size, which is how a file is written for a connector. ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_2}
