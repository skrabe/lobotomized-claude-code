<!--
name: 'Tool Result: Artifact Publish No Host Server Declare Connectors'
description: >-
  Tail of the unreadable-host-grant MCP rejection, telling the model to declare
  only claude.ai connectors or drop mcp.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_NO_HOST_SERVER_DECLARE_CONNECTORS_VAR_0
-->
no host: server can be declared from this session — ${TOOL_RESULT_ARTIFACT_PUBLISH_NO_HOST_SERVER_DECLARE_CONNECTORS_VAR_0.join(", ")}; declare only claude.ai connectors (set "server" to the connector's display name), or to publish without connector access leave "mcp" out of capabilities (pass capabilities: {} to clear a stored declaration).
