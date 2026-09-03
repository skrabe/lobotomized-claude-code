<!--
name: 'Tool result: MCP URL elicitation required'
description: >-
  Model-facing tool_result text returned when an MCP tool call requires URL
  elicitation, telling the model to open the URL and then retry.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_MCP_URL_ELICITATION_REQUIRED_VAR_0
  - TOOL_RESULT_MCP_URL_ELICITATION_REQUIRED_VAR_1
-->
URL elicitation required (open URL, then retry): ${TOOL_RESULT_MCP_URL_ELICITATION_REQUIRED_VAR_0(TOOL_RESULT_MCP_URL_ELICITATION_REQUIRED_VAR_1.urlElicitationDeclined.url)??"[elicitation URL too long to relay — re-run this call in the terminal]"}
