<!--
name: 'System Reminder: REPL MCP server needs auth'
description: >-
  Notes an MCP server needs authentication before its tools answer and that its
  auth tool is callable from a script
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_REPL_MCP_SERVER_NEEDS_AUTH_VAR_0
  - SYSTEM_REMINDER_REPL_MCP_SERVER_NEEDS_AUTH_VAR_1
-->
MCP server ${SYSTEM_REMINDER_REPL_MCP_SERVER_NEEDS_AUTH_VAR_0(SYSTEM_REMINDER_REPL_MCP_SERVER_NEEDS_AUTH_VAR_1.name)} needs authentication before its tools answer; its ${SYSTEM_REMINDER_REPL_MCP_SERVER_NEEDS_AUTH_VAR_1.authTool} tool is callable from a script.
