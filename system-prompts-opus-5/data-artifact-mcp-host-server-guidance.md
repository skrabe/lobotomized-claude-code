<!--
name: 'Data: Artifact MCP host server guidance'
description: >-
  Branch of the Artifact MCP connector guidance telling the model to declare a
  locally-configured MCP server as host:<server> and that only viewers with that
  same local server connected reach it
ccVersion: 2.1.239
-->
 Locally-configured MCP servers connected in this session can also be declared, as host servers: set `server` to `host:<server>` where `<server>` is the segment between `mcp__` and the next `__` in that server's tool names (`mcp__filesystem__read_file` → `host:filesystem`). A host server only answers when the viewer opens the page in a Claude app that has that same local server connected — say so to the user when you publish.
