<!--
name: REPL MCP connected servers list
description: >-
  Note listing connected MCP servers and how to find and call their tools with
  searchTools.
ccVersion: 2.1.328
variables:
  - TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_0
  - TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_1
  - TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_2
  - TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_3
-->
${TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_0} connected servers are ${TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_1.slice(0,TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_2).join(", ")}${TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_3>0?` and ${TOOL_DESCRIPTION_REPL_MCP_SERVERS_LIST_VAR_3} more`:""}. Find a tool with \`searchTools\`, then call it with the input its match shows.
