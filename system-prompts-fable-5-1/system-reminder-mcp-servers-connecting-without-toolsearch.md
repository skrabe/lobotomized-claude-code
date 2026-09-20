<!--
name: 'System Reminder: MCP servers connecting without ToolSearch'
description: >-
  Lists MCP servers still connecting when ToolSearch is absent and tells the
  agent to await tool announcements rather than report the capability
  unavailable
ccVersion: 2.1.277
variables:
  - PENDING_MCP_SERVERS
-->
The following MCP servers are still connecting — their tools (typically named mcp__<server>__*) are not yet available but will be announced here once they connect:
${PENDING_MCP_SERVERS}

If the user's request might be served by one of these servers (even if they didn't name it explicitly), do not report the capability as unavailable while they are still connecting.
