<!--
name: 'Tool Description: ReadMcpResourceDirTool'
description: >-
  Short description of the ReadMcpResourceDirTool that lists the direct children
  of an MCP directory resource
ccVersion: 2.1.187
-->

List the direct children of a directory resource on an MCP server.
- server: The name of the MCP server to read from
- uri: The URI of the directory resource

Only usable against a server that has declared support for directory listing. The listing is not recursive.
