<!--
name: 'Slash command: /plugin validate MCP servers array'
description: >-
  Validation warning that mcpServers is an array keyed by index and should be an
  object keyed by server name.
ccVersion: 2.1.281
-->
is an array; the plugin loader keys its servers by array index ("0", "1", ...), and review tooling has misread this shape as 'no servers'. Use an object keyed by server name.
