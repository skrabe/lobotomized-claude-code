<!--
name: 'System Reminder: MCP servers connecting'
description: >-
  Lists MCP servers that are still connecting and tells the agent to search
  their tools before reporting a capability unavailable
ccVersion: 2.1.178
variables:
  - PENDING_MCP_SERVERS
  - TOOL_SEARCH_TOOL_NAME
-->
The following MCP servers are still connecting — their tools (named mcp__<server>__*) are not yet available but will appear shortly:
${PENDING_MCP_SERVERS}

If the user's request might be served by one of these (even if not named), call ${TOOL_SEARCH_TOOL_NAME} with a relevant keyword — it waits for connecting servers and searches their tools once available. Don't report a capability as unavailable without searching first.
