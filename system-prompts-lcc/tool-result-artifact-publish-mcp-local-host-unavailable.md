<!--
name: Artifact Publish MCP Local Host Unavailable
description: >-
  Publish capabilities error when a locally-configured MCP server is named but
  host servers are unavailable in this session.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_HOST_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_HOST_UNAVAILABLE_VAR_1
-->
"${TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_HOST_UNAVAILABLE_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_MCP_LOCAL_HOST_UNAVAILABLE_VAR_1.server,{max:70})}" names a locally-configured MCP server, and host servers aren't available in this session — declare only claude.ai connectors (set "server" to the connector's display name), or ${'to publish without connector access leave "mcp" out of capabilities (pass capabilities: {} to clear a stored declaration)'}
