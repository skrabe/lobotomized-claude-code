<!--
name: 'Tool Result: MCP connector file object written in argument'
description: >-
  Refuses a connector call whose argument holds a file object (id, mimeType,
  size), says no file is sent that way and not to retry with one
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_1
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_0} was not called: the argument ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_1} holds an object with an id, a mimeType and a size, which is how a file is written for a connector. Claude Code sends no file through ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_1} and does not pass such an object on. Do not retry with one there. Tell the user if they asked for a file to go this way. A call with no such object in ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_VAR_1} is still sent.
