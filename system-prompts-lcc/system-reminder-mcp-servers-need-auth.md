<!--
name: 'System Reminder: MCP servers need authentication'
description: >-
  Lists MCP servers that need authentication before their tools can be used, and
  tells the model to ask the user to authorize them without requesting codes,
  tokens or callback URLs
ccVersion: 2.1.282
variables:
  - SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_0
  - SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_1
  - SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_2
-->
The following MCP servers require authentication before their tools can be used:
${SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_0}

${SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_1} Tell the user that these servers need to be authorized — ${SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_2} — and that the capability is unavailable until they do. Do not ask the user for authorization codes, tokens, or callback URLs.
