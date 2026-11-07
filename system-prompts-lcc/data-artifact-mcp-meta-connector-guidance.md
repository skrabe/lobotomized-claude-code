<!--
name: 'Data: Artifact MCP meta-connector guidance'
description: >-
  Branch of the Artifact MCP connector guidance covering the built-in claude.ai
  meta connector: declare its exact server name, viewer-side calls have no
  calling session, and features must stay optional because viewers may have
  fewer tools.
ccVersion: 2.1.319
variables:
  - DATA_ARTIFACT_MCP_META_CONNECTOR_GUIDANCE_VAR_0
-->
 A page can call the \`mcp__${DATA_ARTIFACT_MCP_META_CONNECTOR_GUIDANCE_VAR_0.toolPrefix}__*\` tools in your tool list through the built-in claude.ai connector \`${DATA_ARTIFACT_MCP_META_CONNECTOR_GUIDANCE_VAR_0.server}\`: declare that exact name as \`server\` with those tools' upstream names. A published page calls them as the viewer, with no calling session, so tools that act on the calling session (e.g. \`send_later\`, \`watch_url\`) do not apply there. A viewer may have fewer of the connector's tools than you (often only a core set for managing routines), so keep each feature optional: only after the viewer has allowed the connector, have the page call \`listTools()\`. When a tool a feature needs is not listed, or a call to it rejects with code \`blocked_by_policy\`, show that feature as unavailable and do not call that tool.
