<!--
name: 'Data: Artifact MCP named opaque connector mapping'
description: >-
  Clause of the Artifact MCP connector guidance listing opaque connector ids
  with display names and telling the model to set `server` to that name, never
  the id.
ccVersion: 2.1.246
variables:
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_0
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_1
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_2
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_3
  - DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_4
-->
 The ids belong to these connectors: ${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_0.join("; ")}${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_1(DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_2.named.length,DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_0.length,"ask the user for their names")}. For these, set \`server\` to the connector's name exactly as written here, e.g. \`{"server": "${DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_3(DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_2.named[0]?.DATA_ARTIFACT_MCP_CONNECTOR_OPAQUE_NAMED_VAR_4??"")}", "tools": [...]}\` — never the id or any \`mcp__\` segment — and in the page pass that same name as the \`server\` argument of \`callTool\`/\`watchTool\`, because viewers resolve connectors by name only.
