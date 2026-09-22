<!--
name: Artifact Publish Mcp Connector As Host
description: >-
  MCP manifest rejection when a claude.ai connector was named as if it were a
  local host server.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_CONNECTOR_AS_HOST_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_CONNECTOR_AS_HOST_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_CONNECTOR_AS_HOST_VAR_2
-->
"${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_CONNECTOR_AS_HOST_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_MCP_CONNECTOR_AS_HOST_VAR_1.server,{max:70})}" names the claude.ai connector "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_CONNECTOR_AS_HOST_VAR_2}", not a local server — declare it as {"server": "${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_CONNECTOR_AS_HOST_VAR_2}", "tools": [...]} and call it by that name in the page
