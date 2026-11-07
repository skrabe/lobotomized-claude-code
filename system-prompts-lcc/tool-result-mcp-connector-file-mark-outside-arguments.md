<!--
name: 'Tool Result: MCP connector schema file mark outside arguments'
description: >-
  Refuses every call of a tool whose schema asks for a file in an unsendable
  form with no identifiable argument
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_OUTSIDE_ARGUMENTS_VAR_0
-->
${TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_OUTSIDE_ARGUMENTS_VAR_0} was not called: this connector's schema asks for a file in a form Claude Code cannot send, and Claude Code cannot tell which argument would carry it, so it sends no call of this tool. Do not retry. Tell the user; the connector's maker has to change this.
