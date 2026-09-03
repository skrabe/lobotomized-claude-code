<!--
name: 'System Reminder: Deferred tools readded non-MCP'
description: >-
  Reminder that deferred non-MCP tools announced earlier are available again in
  this session and should be loaded via ToolSearch.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0
  - SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_1
-->
${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0.other.length} deferred tool${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0.other.length===1?" is":"s are"} available again in this session (announced earlier in this conversation): ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_0.other.join(", ")}. Load via ${SYSTEM_REMINDER_DEFERRED_TOOLS_READDED_NON_MCP_VAR_1} as before.
