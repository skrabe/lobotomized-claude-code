<!--
name: 'Tool Result: Connector file object not passed on'
description: >-
  Explanation slot for a connector file object in an argument with no file
  support: Claude Code does not send or pass it, do not retry, tell the user.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_NOT_PASSED_VAR_0
-->
Claude Code sends no file through ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_NOT_PASSED_VAR_0} and does not pass such an object on. Do not retry with one there. Tell the user if they asked for a file to go this way. A call with no such object in ${TOOL_RESULT_MCP_CONNECTOR_FILE_OBJECT_IN_ARGUMENT_NOT_PASSED_VAR_0} is still sent.
