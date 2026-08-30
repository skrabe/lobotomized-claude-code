<!--
name: 'System Reminder: Deferred tools available again'
description: Reminder that deferred MCP tools are available again after a server reconnect.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_1
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_2
-->
${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0.mcp.length} deferred tool${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0.mcp.length===1?" is":"s are"} available again (MCP server reconnected — names announced earlier in this conversation): ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_1(SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_0.mcp)}. Load via ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_VAR_2} as before.
