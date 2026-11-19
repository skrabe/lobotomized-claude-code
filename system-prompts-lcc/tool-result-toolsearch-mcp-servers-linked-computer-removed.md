<!--
name: 'Tool Result: ToolSearch MCP servers linked computer removed'
description: >-
  ToolSearch no-match note that an MCP server's tools are unavailable because
  the computer linked to the session was removed from the account
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_LINKED_COMPUTER_REMOVED_VAR_0
  - TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_LINKED_COMPUTER_REMOVED_VAR_1
-->
${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_LINKED_COMPUTER_REMOVED_VAR_0.endsWith(".")?"":"."} Note: when this search ran, the computer linked to this session had been removed from the user's account. The tools of the MCP server ${TOOL_RESULT_TOOLSEARCH_MCP_SERVERS_LINKED_COMPUTER_REMOVED_VAR_1} reach that computer, so they are unavailable while the session stays linked to it. This is not a connection failure.
