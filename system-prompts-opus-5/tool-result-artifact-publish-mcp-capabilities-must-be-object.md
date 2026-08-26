<!--
name: Artifact Publish Mcp Capabilities Must Be Object
description: >-
  MCP manifest rejection when capabilities.mcp is not an object of
  {servers:[...]} form.
ccVersion: 2.1.246
-->
capabilities.mcp must be an object of the form {"servers": [${'{"server": "<connector name>", "tools": ["<tool name>", ...]}'}]} — not an array, a string, or any other shape; ${'to publish without connector access leave "mcp" out of capabilities (pass capabilities: {} to clear a stored declaration)'}
