<!--
name: 'Data: Artifact MCP undeclarable connector names'
description: >-
  Clause telling the model that some connector display names cannot be declared
  as manifest `server` until renamed in claude.ai.
ccVersion: 2.1.251
variables:
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_0
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_2
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_3
-->
 ${DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_0(DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1.length,"Connector")} ${DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1.join(", ")}${DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_2(DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_3.undeclarable.length,DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1.length,"more like them")} cannot be declared at all until renamed: a manifest \`server\` must be 1–64 characters with no control characters, line breaks, unusual spaces or text-direction controls, must not begin or end with a space or invisible character, and must not read as \`host:\` or be shaped like an id or a \`claude_ai_…\`/\`mcp__…\` prefix, so if the page needs one of these, tell the user it must first be renamed in claude.ai (Settings → Connectors).
