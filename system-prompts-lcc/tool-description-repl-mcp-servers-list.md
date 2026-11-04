<!--
name: 'Tool Description: REPL connected MCP servers'
description: >-
  Lists connected MCP servers and says to find tools with searchTools then call
  them
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_0
  - TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_1
-->
MCP tools: connected servers are ${TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_0.join(", ")}${TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_1>0?` and ${TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_1} more`:""}. Find a tool with \`searchTools\`, then call it with the input its match shows.
