<!--
name: 'System Reminder: MCP servers failed to connect'
description: >-
  Lists configured MCP servers that failed to connect and tells the agent to
  treat their tools as unavailable because of a connection failure
ccVersion: 2.1.295
variables:
  - UNAVAILABILITY_SCOPE_PHRASE
  - FAILED_MCP_SERVERS
  - FAILED_MCP_SERVERS_OVERFLOW_SUFFIX
-->
The following MCP servers are configured but failed to connect — their tools (typically named mcp__<server>__*) are unavailable ${UNAVAILABILITY_SCOPE_PHRASE}:
${FAILED_MCP_SERVERS}${FAILED_MCP_SERVERS_OVERFLOW_SUFFIX}
