<!--
name: 'Tool Result: Connector file object, write path instead'
description: >-
  Explanation slot for a connector file object written in an argument that takes
  a hidden file path: the object is not passed on, and the file should be
  written as its path.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_WRITE_PATH_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_WRITE_PATH_VAR_1
-->
Claude Code does not pass such an object on; a call with none in ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_WRITE_PATH_VAR_0} is still sent. To send a file on this computer there, write it as ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_WRITE_PATH_VAR_1}, its path.
