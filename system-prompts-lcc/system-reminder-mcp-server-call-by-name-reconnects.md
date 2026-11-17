<!--
name: 'System Reminder: MCP server reconnects on call by name'
description: >-
  Clause explaining that calling a server's tool by name, or a search query
  naming the server, connects to it again
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_MCP_SERVER_CALL_BY_NAME_RECONNECTS_VAR_0
  - SYSTEM_REMINDER_MCP_SERVER_CALL_BY_NAME_RECONNECTS_VAR_1
  - SYSTEM_REMINDER_MCP_SERVER_CALL_BY_NAME_RECONNECTS_VAR_2
-->
calling one of a server's tools by name (mcp__<server>__<tool>)${SYSTEM_REMINDER_MCP_SERVER_CALL_BY_NAME_RECONNECTS_VAR_0||SYSTEM_REMINDER_MCP_SERVER_CALL_BY_NAME_RECONNECTS_VAR_1.searchMayBeAbsent===!0?"":`, or a ${SYSTEM_REMINDER_MCP_SERVER_CALL_BY_NAME_RECONNECTS_VAR_2} query that contains the server's name,`} connects to it again
