<!--
name: 'Data: Artifact MCP unnamed opaque connectors'
description: >-
  Clause telling the model to ask the user for each unnamed opaque connector's
  claude.ai display name and to use that name as `server`.
ccVersion: 2.1.246
variables:
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_0
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_1
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_2
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_3
-->
 ${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_0?"Connector":"Connectors"} ${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_1.join(", ")}${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_2(DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_3.unnamedIds.length,DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_1.length,"treat the rest the same way")} did not report ${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_0?"a name":"names"} here: ask the user for ${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_0?"that connector's":"each connector's"} name exactly as shown in claude.ai (Settings → Connectors) — describe ${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_UNNAMED_VAR_0?"it":"each"} by the tools it provides (its \`mcp__<id>__…\` tool names), since the user cannot see the id — and use that name as \`server\` and in the page's calls; the id itself is refused at publish because no viewer can resolve it.
