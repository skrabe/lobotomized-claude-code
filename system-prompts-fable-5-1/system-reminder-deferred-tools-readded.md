<!--
name: 'System Reminder: Deferred Tools Available Again'
description: >-
  deferred_tools_delta meta line announcing MCP tools available again after a
  server reconnect; wording is deferred tool(s) when ToolSearch is present,
  otherwise tool(s).
ccVersion: 2.1.265
variables:
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_1
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_2
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_3
-->
${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0.mcp.length} ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_1}${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0.mcp.length===1?" is":"s are"} available again (MCP server reconnected — names announced earlier in this conversation): ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_2(SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0.mcp)}.${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_3}
