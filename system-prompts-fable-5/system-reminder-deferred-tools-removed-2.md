<!--
name: 'System Reminder: Deferred tools no longer available'
description: >-
  reminder that deferred tools are gone because their MCP server disconnected
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_2_VAR_0
  - SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_2_VAR_1
-->
These deferred tools are no longer available (their MCP server disconnected) — ${SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_2_VAR_0} won't find them:
${SYSTEM_REMINDER_DEFERRED_TOOLS_REMOVED_2_VAR_1.mcp.join(`\n`)}
