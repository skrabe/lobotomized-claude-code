<!--
name: 'Tool Result: MCP connector schema file argument unsendable'
description: >-
  Refuses a call setting an argument that may carry a file in an unsendable form
  while allowing calls that omit it
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_UNFILLED_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_UNFILLED_VAR_1
  - TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_UNFILLED_VAR_2
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_UNFILLED_VAR_0} was not called: this connector's schema asks for a file in a form Claude Code cannot send, and the argument ${TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_UNFILLED_VAR_1(TOOL_RESULT_MCP_CONNECTOR_FILE_MARK_UNFILLED_VAR_2)} may carry one. Do not retry with that argument set. Tell the user; the connector's maker has to change this. A call that leaves it out is still sent.
