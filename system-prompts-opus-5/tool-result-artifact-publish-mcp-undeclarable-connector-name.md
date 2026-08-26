<!--
name: Artifact Publish Mcp Undeclarable Connector Name
description: >-
  MCP manifest rejection when a connector cannot be declared until the user
  renames it in claude.ai Settings.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_1
-->
connector "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_1.name)}" cannot be declared until it is renamed in claude.ai (Settings → Connectors): a manifest "server" may only contain letters, digits, spaces and . _ ( ) - (64 at most, no surrounding spaces, no invisible or quote-like characters, not shaped like an id or a claude_ai_/mcp__ prefix) — tell the user
