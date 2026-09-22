<!--
name: 'Data: Artifact MCP valid servers — no app or local'
description: >-
  Valid-`server` branch (no meta connector, hosted connectors present)
  restricting the model to claude.ai connectors and excluding the Claude app's
  own servers and local MCP servers.
ccVersion: 2.1.246
-->
 Only claude.ai connectors are valid `server` values — the Claude app's own servers (`cowork`, `workspace`, `scheduled-tasks`, `session_info` and the like) and other locally-configured MCP servers in your tool list are not.
