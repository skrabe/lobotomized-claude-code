<!--
name: Artifact Publish Mcp Known Connector Id
description: >-
  MCP manifest rejection when server is the id of a known connector and must be
  replaced with that connector's name.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_KNOWN_CONNECTOR_ID_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_KNOWN_CONNECTOR_ID_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_KNOWN_CONNECTOR_ID_VAR_2
-->
"${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_KNOWN_CONNECTOR_ID_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_MCP_KNOWN_CONNECTOR_ID_VAR_1.server)}" is the id of connector "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_KNOWN_CONNECTOR_ID_VAR_2}" — set "server" to "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_KNOWN_CONNECTOR_ID_VAR_2}": approval prompts and viewers know connectors by name only, and the page must call it by that name too
