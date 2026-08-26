<!--
name: Artifact Publish Mcp Opaque Connector Id
description: >-
  MCP manifest rejection when server is a connector id viewers cannot resolve;
  the model must use the claude.ai display name.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_OPAQUE_CONNECTOR_ID_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_OPAQUE_CONNECTOR_ID_VAR_1
-->
"${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_OPAQUE_CONNECTOR_ID_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_MCP_OPAQUE_CONNECTOR_ID_VAR_1.server,{max:70})}" is a connector id, which no viewer can resolve — set "server" to that connector's name exactly as shown in claude.ai (Settings → Connectors) and pass the same name to callTool/watchTool in the page; if you don't know the name, ask the user, describing the connector by its tools (the user cannot see the id)
