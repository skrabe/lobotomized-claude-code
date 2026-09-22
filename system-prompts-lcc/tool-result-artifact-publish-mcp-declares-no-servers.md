<!--
name: Artifact Publish Mcp Declares No Servers
description: MCP manifest rejection when capabilities.mcp.servers is empty.
ccVersion: 2.1.246
-->
capabilities.mcp declares no servers — put one ${'{"server": "<connector name>", "tools": ["<tool name>", ...]}'} entry under "servers" for each connector the page calls; ${'to publish without connector access leave "mcp" out of capabilities (pass capabilities: {} to clear a stored declaration)'} — an empty "servers" list is always refused
