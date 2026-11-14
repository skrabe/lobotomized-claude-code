<!--
name: 'Tool result: mcp_tool hook refused for subagent or background session'
description: >-
  mcp_tool hook refusal when a subagent or background session may have fired the
  hook, so the server would misattribute the call
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_TOOL_HOOK_SUBAGENT_OR_BACKGROUND_REFUSED_VAR_0
-->
Hooks can't call MCP server '${TOOL_RESULT_MCP_TOOL_HOOK_SUBAGENT_OR_BACKGROUND_REFUSED_VAR_0.name}' when a subagent or a background session may have fired them, because the server would read the call as the main session's. Point this hook at another server.
