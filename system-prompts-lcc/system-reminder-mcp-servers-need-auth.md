<!--
name: 'System Reminder: MCP servers need authentication'
description: >-
  Meta message telling Claude that listed MCP servers require auth before their
  tools work and to instruct the user to authorize them.
ccVersion: 2.1.196
variables:
  - SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_0
-->
The following MCP servers require authentication before their tools can be used:
${SYSTEM_REMINDER_MCP_SERVERS_NEED_AUTH_VAR_0}

This session is non-interactive, so Claude cannot run the OAuth flow here. Tell the user that these servers need to be authorized — for claude.ai connectors, via their claude.ai connector settings; for other servers, via \`claude mcp\` or /mcp in an interactive session — and that the capability is unavailable until they do. Do not ask the user for authorization codes, tokens, or callback URLs.
