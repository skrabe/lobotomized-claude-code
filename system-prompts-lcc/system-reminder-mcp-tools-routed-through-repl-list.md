<!--
name: 'System Reminder: MCP tools routed through REPL (list form)'
description: >-
  Lists previously announced MCP tools that are no longer directly callable
  because this surface routes them through the REPL, where they remain available
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_LIST_VAR_0
  - SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_LIST_VAR_1
  - SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_LIST_VAR_2
-->
The following previously-announced MCP tools are ${SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_LIST_VAR_0} in this session (this surface routes MCP tools through the REPL instead). Their MCP servers remain connected and the tools stay available inside the REPL environment. ${SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_LIST_VAR_1}:
${SYSTEM_REMINDER_MCP_TOOLS_ROUTED_THROUGH_REPL_LIST_VAR_2.join(`
`)}
