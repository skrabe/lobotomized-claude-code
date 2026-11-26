<!--
name: 'Slash Command: Schedule Local MCP Not Attachable'
description: >-
  ConnectorsInfo line in the /schedule cloud-agents prompt stating Claude
  Code-configured MCP servers cannot be attached to cloud routines.
ccVersion: 2.1.332
-->
Note that MCP servers configured directly in Claude Code (e.g. with `claude mcp add`) cannot be attached to cloud scheduled tasks, which can only use claude.ai connectors.
