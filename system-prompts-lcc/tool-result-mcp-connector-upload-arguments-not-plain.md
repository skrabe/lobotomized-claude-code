<!--
name: Connector call arguments not copyable
description: >-
  Explains the call's arguments could not be copied and checked, and asks for
  fewer or flatter arguments.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ARGUMENTS_NOT_PLAIN_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ARGUMENTS_NOT_PLAIN_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ARGUMENTS_NOT_PLAIN_VAR_0(TOOL_RESULT_MCP_CONNECTOR_UPLOAD_ARGUMENTS_NOT_PLAIN_VAR_1)} Claude Code could not make a copy of this call's arguments, and it calls a connector's tool that takes files only with arguments it has copied and checked. Arguments that hold very many values, or lists and objects nested very deeply, cannot be copied: make the call with fewer or flatter ones. If these are neither, this is a bug in Claude Code that the user cannot fix.
