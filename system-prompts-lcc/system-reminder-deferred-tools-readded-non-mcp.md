<!--
name: 'System Reminder: Deferred Tools Readded Non-MCP'
description: >-
  deferred_tools_delta meta line announcing non-MCP tools available again in
  this session; wording is deferred tool(s) when ToolSearch is present,
  otherwise tool(s).
ccVersion: 2.1.265
variables:
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_1
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_2
-->
${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0.other.length} ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_1}${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0.other.length===1?" is":"s are"} available again in this session (announced earlier in this conversation): ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0.other.join(", ")}.${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_2}
