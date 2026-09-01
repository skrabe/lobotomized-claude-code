<!--
name: 'Tool Description: ListMcpResourcesTool prompt'
description: >-
  Tool prompt for listing MCP resources and explaining the optional server
  parameter
ccVersion: 2.1.178
-->
List available resources from configured MCP servers. Each returned resource includes a 'server' field indicating which server it belongs to.

Parameters:
- server (optional): Name of a specific MCP server to query. If omitted, resources from all servers are returned.
