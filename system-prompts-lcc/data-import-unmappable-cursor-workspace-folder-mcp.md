<!--
name: 'Data: Import Unmappable Cursor workspaceFolder MCP'
description: >-
  Unmappable reason when a Cursor user-scope MCP server references
  ${workspaceFolder}, interpolated into the /import summary prompt.
ccVersion: 2.1.265
-->
References `${workspaceFolder}` — per-workspace in Cursor, but Claude Code's user-scope MCP servers are global. Importing would pin it to this checkout and run it in every project. Add it as a project-scope server (in the specific project's .mcp.json) instead.
