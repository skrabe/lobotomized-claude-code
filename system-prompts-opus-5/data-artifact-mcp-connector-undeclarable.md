<!--
name: 'Data: Artifact MCP undeclarable connector names'
description: >-
  Clause telling the model that some connector display names cannot be declared
  as manifest `server` until renamed in claude.ai.
ccVersion: 2.1.246
variables:
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_0
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_2
  - DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_3
-->
 ${DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_0(DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1.length,"Connector")} ${DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1.join(", ")}${DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_2(DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_3.undeclarable.length,DATA_ARTIFACT_MCP_CONNECTOR_UNDECLARABLE_VAR_1.length,"more like them")} cannot be declared at all until renamed: a manifest \`server\` may only contain letters, digits, spaces and \`. _ ( ) -\` (64 at most, no surrounding spaces, no invisible or quote-like characters, and not shaped like an id or a \`claude_ai_…\`/\`mcp__…\` prefix), so if the page needs one of these, tell the user it must first be renamed in claude.ai (Settings → Connectors).
