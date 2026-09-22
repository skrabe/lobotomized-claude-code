<!--
name: 'Data: Artifact MCP meta-connector guidance'
description: >-
  Branch of the Artifact MCP connector guidance covering the built-in claude.ai
  meta connector, telling the model to declare its exact server name and that
  viewer-side calls have no calling session
ccVersion: 2.1.239
variables:
  - DATA_ARTIFACT_MCP_META_CONNECTOR_GUIDANCE_VAR_0
-->
 The \`mcp__${DATA_ARTIFACT_MCP_META_CONNECTOR_GUIDANCE_VAR_0.toolPrefix}__*\` tools in your tool list are also available to viewers as the built-in claude.ai connector \`${DATA_ARTIFACT_MCP_META_CONNECTOR_GUIDANCE_VAR_0.server}\`: declare that exact name as \`server\` with those tools' upstream names. A published page calls them as the viewer, with no calling session, so tools that act on the calling session (e.g. \`send_later\`, \`watch_url\`) do not apply there.
