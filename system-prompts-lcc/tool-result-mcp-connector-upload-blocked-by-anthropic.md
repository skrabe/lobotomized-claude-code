<!--
name: 'Tool Result: MCP connector upload blocked by Anthropic'
description: >-
  Upload refusal when Anthropic doesn't allow sending files to this connector or
  couldn't confirm the org may reach it.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BLOCKED_BY_ANTHROPIC_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BLOCKED_BY_ANTHROPIC_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BLOCKED_BY_ANTHROPIC_VAR_0} was not sent: Anthropic doesn't allow Claude to send files to this connector, or couldn't confirm that this organization may reach it. Do not retry. Tell the user. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_BLOCKED_BY_ANTHROPIC_VAR_1}
