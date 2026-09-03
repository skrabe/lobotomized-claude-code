<!--
name: 'System Reminder: Deferred Tools Removed (Count Summary)'
description: >-
  Meta user message injected when more than the display cap of deferred MCP
  tools disappear at once, telling Claude not to search for them via ToolSearch.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_SUMMARY_VAR_0
  - SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_SUMMARY_VAR_1
  - SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_SUMMARY_VAR_2
-->
${SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_SUMMARY_VAR_0.mcp.length} deferred tools are no longer available (MCP server disconnected): ${SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_SUMMARY_VAR_1(SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_SUMMARY_VAR_0.mcp)}. ${SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_SUMMARY_VAR_2} won't find them.
