<!--
name: 'System Reminder: MCP servers tool listing failed'
description: >-
  Lists connected MCP servers whose tool listing failed and tells the model not
  to conclude they have no tools and to inform the user
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_0
  - SYSTEM_REMINDER_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_1
-->
The following MCP servers are connected, but listing their tools failed — their tools (typically named mcp__<server>__*) are unavailable for now:
${SYSTEM_REMINDER_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_0}${SYSTEM_REMINDER_MCP_SERVERS_TOOL_LISTING_FAILED_VAR_1}

Treat this as a failure to load their tools, not a missing capability — do not conclude the server has no tools. If the user's request depends on one of these servers, tell them that this server's tools could not be loaded.
