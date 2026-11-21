<!--
name: 'Data: deniedMcpServers.serverUrl setting description'
description: >-
  Description of the `deniedMcpServers.serverUrl` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.330
-->
URL pattern with wildcard support (e.g., "https://*.example.com/*") for blocked remote MCP servers. A pattern with no query also blocks the URL with any query, or with a trailing slash added or, if its path has no wildcard, removed.
