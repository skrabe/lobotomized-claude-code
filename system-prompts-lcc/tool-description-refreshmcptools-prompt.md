<!--
name: 'Tool Description: RefreshMcpTools prompt'
description: >-
  Tool prompt for refreshing one or all connected MCP servers tool lists and
  interpreting per-server results
ccVersion: 2.1.211
-->
Re-query the tool lists of connected MCP servers and update the available tools.

Returns one entry per server: the server name, refresh status, current tool count, and which tool names were added or removed relative to what was previously available. Servers that are not currently connected are reported as not_connected — this tool never dials or re-dials a connection, it only re-reads the tool list over an existing one.
