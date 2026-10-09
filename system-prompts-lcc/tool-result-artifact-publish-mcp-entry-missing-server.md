<!--
name: 'Tool Result: Artifact publish MCP entry missing server'
description: >-
  Validation error when an MCP servers entry has no server string, showing the
  expected entry shape
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_ENTRY_MISSING_SERVER_VAR_0
-->
servers[${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_ENTRY_MISSING_SERVER_VAR_0.index}] has no "server" string — each entry is ${'{"server": "<connector name>", "tools": ["<tool name>", ...]}'}
