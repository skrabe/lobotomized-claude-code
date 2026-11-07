<!--
name: 'Tool Result: MCP connector call has unlisted argument'
description: >-
  Refuses a file-taking connector call with an argument the schema does not list
  and says to retry with only listed arguments
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENT_NOT_LISTED_VAR_0
-->
No file was sent and ${TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENT_NOT_LISTED_VAR_0} was not called: this call has an argument that ${TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENT_NOT_LISTED_VAR_0} does not list. You were asked for a file's path for ${TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENT_NOT_LISTED_VAR_0}, and the name of an argument is sent to the connector as text too, so Claude Code sends ${TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENT_NOT_LISTED_VAR_0} only the arguments it lists. Do not retry with that argument; you may call ${TOOL_RESULT_MCP_CONNECTOR_FILE_ARGUMENT_NOT_LISTED_VAR_0} with the arguments it lists.
