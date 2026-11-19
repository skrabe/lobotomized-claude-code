<!--
name: '/import MCP add: .mcp.json has top-level servers'
description: >-
  Refusal when adding to .mcp.json would hide servers listed at its top level;
  tells how to move them under mcpServers.
ccVersion: 2.1.328
-->
Can't add to .mcp.json: it lists servers at the top level, and adding an "mcpServers" key would stop a plugin from loading them. Move them under "mcpServers", then try again. If they aren't servers, add "mcpServers": {} to the file instead.
