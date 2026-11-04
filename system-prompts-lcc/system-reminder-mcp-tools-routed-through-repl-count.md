<!--
name: 'System Reminder: MCP tools routed through REPL (count form)'
description: >-
  Tells the model that a counted set of previously announced MCP tools are no
  longer directly callable because this surface routes them through the REPL,
  where they remain available
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_0
  - SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_1
  - SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_2
  - SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_3
-->
${SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_0.length} previously-announced MCP tools are ${SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_1} in this session (this surface routes MCP tools through the REPL instead): ${SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_2(SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_0)}. Their MCP servers remain connected and the tools stay available inside the REPL environment. ${SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_COUNT_VAR_3}.
