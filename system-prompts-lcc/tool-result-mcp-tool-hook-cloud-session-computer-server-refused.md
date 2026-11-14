<!--
name: 'Tool result: mcp_tool hook refused in cloud session'
description: >-
  mcp_tool hook refusal in a cloud session for a server that acts on the user's
  computer or browser, since hook calls skip the permission check
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_TOOL_HOOK_CLOUD_SESSION_COMPUTER_SERVER_REFUSED_VAR_0
-->
Hooks can't call tools of MCP server '${TOOL_RESULT_MCP_TOOL_HOOK_CLOUD_SESSION_COMPUTER_SERVER_REFUSED_VAR_0}' in a cloud session, because that server acts on your computer or browser and a hook's call skips the permission check. Remove this mcp_tool hook or point it at another server.
