<!--
name: 'Slash Command: /plugin validate MCP server url without type'
description: >-
  Plugin validator error: a server has a url but no type, so it is parsed as a
  stdio server and silently dropped.
ccVersion: 2.1.281
-->
server has a "url" but no "type". Remote servers must set "type" to "http" (or "sse" / "ws"); without it the entry is parsed as a stdio server, fails for lacking "command", and is silently dropped at load.
