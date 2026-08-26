<!--
name: 'Tool Result: Artifact Publish MCP Internal Host Servers'
description: >-
  Clause of the mcp-manifest-rejected Artifact publish error when the manifest
  names Claude's built-in servers as host servers.
ccVersion: 2.1.246
-->
pages as host servers; declare only servers from the MCP configuration (host:<name> for the `mcp__<name>__<tool>` tools of a server you configured). The control plane would accept this manifest, but the page would break at view time
