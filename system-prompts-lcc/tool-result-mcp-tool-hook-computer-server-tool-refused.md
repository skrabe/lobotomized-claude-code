<!--
name: 'Tool Result: mcp_tool hook refused a computer MCP server tool'
description: >-
  Refusal when an mcp_tool hook tries to call a tool of an MCP server that acts
  on the user's computer or browser from this session
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_MCP_TOOL_HOOK_COMPUTER_SERVER_TOOL_REFUSED_VAR_0
  - TOOL_RESULT_MCP_TOOL_HOOK_COMPUTER_SERVER_TOOL_REFUSED_VAR_1
-->
Hooks can't call '${TOOL_RESULT_MCP_TOOL_HOOK_COMPUTER_SERVER_TOOL_REFUSED_VAR_0}' of MCP server '${TOOL_RESULT_MCP_TOOL_HOOK_COMPUTER_SERVER_TOOL_REFUSED_VAR_1.name}' from this session, because that server acts on your computer or browser and a hook's call skips the permission check. Remove this mcp_tool hook or point it at another server.
