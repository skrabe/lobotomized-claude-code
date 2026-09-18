<!--
name: 'Data: allowedMcpServers setting'
description: >-
  Describes how the enterprise allowedMcpServers setting governs user-added
  versus organization-delivered MCP servers, including ${VAR} expansion,
  undefined and empty-array behavior, and denylist precedence
ccVersion: 2.1.276
-->
Enterprise allowlist of the MCP servers users may use. Governs servers users add (user, project and local config, --mcp-config, agent frontmatter, plugins, claude.ai connectors); servers the organization itself delivers (managedMcpServers, and managed-mcp.json entries that use no ${VAR} expansion) are allowed without being listed; a managed-mcp.json entry that uses ${VAR} expansion is still checked against this list. If undefined, all servers are allowed. If empty array, users can use no servers of their own. Denylist takes precedence - if a server is on both lists, it is denied.
