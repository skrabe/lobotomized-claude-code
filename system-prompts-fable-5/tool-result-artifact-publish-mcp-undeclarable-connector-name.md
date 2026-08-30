<!--
name: Artifact Publish Mcp Undeclarable Connector Name
description: >-
  MCP manifest rejection when a connector cannot be declared until the user
  renames it in claude.ai Settings.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_1
-->
connector "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_MCP_UNDECLARABLE_CONNECTOR_NAME_VAR_1.name)}" cannot be declared until it is renamed in claude.ai (Settings → Connectors): a manifest "server" must be 1–64 characters with no control characters, line breaks, unusual spaces or text-direction controls, must not begin or end with a space or invisible character, and must not read as host: or be shaped like an id or a claude_ai_/mcp__ prefix — tell the user
