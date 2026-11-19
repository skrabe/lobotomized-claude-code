<!--
name: 'System reminder: REPL MCP servers still connecting'
description: >-
  Note that some MCP servers are still connecting, so their tools can't be found
  yet, and the script should wait and search again.
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_REPL_MCP_SERVERS_STILL_CONNECTING_VAR_0
  - SYSTEM_REMINDER_REPL_MCP_SERVERS_STILL_CONNECTING_VAR_1
  - SYSTEM_REMINDER_REPL_MCP_SERVERS_STILL_CONNECTING_VAR_2
-->
${SYSTEM_REMINDER_REPL_MCP_SERVERS_STILL_CONNECTING_VAR_0} ${SYSTEM_REMINDER_REPL_MCP_SERVERS_STILL_CONNECTING_VAR_1.slice(0,SYSTEM_REMINDER_REPL_MCP_SERVERS_STILL_CONNECTING_VAR_2).join(", ")}. Their tools can't be found or called yet. If the request may need one, wait a few seconds in a script, then search in the next script.
