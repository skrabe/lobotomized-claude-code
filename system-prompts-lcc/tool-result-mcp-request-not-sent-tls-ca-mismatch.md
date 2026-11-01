<!--
name: 'Tool result: MCP request not sent (TLS CA mismatch)'
description: >-
  Error returned when an MCP request is blocked because the server's trusted CA
  list no longer overlaps Claude Code's current TLS settings
ccVersion: 2.1.316
-->
MCP request not sent: its list of trusted CA certificates has nothing in common with the one Claude Code uses now, most likely because Claude Code's TLS settings changed after the server connected. Reconnect the server to use the new settings.
