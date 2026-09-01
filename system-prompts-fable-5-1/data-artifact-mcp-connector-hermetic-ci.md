<!--
name: 'Data: Artifact MCP Connector Hermetic/CI Fetch'
description: >-
  Hermetic/CI clause of the Artifact MCP connector guidance: fetch
  /v1/mcp_servers with $CLAUDE_CODE_OAUTH_TOKEN and use each entry's
  display_name as `server`.
ccVersion: 2.1.246
variables:
  - DATA_ARTIFACT_MCP_CONNECTOR_HERMETIC_CI_VAR_0
  - DATA_ARTIFACT_MCP_CONNECTOR_HERMETIC_CI_VAR_1
-->
 In hermetic/CI sessions where connectors aren't loaded but \`$CLAUDE_CODE_OAUTH_TOKEN\` is set, fetch the list via Bash: \`curl -H 'anthropic-version: 2023-06-01' -H 'anthropic-beta: ${DATA_ARTIFACT_MCP_CONNECTOR_HERMETIC_CI_VAR_0.header}' -H "Authorization: Bearer $CLAUDE_CODE_OAUTH_TOKEN" ${DATA_ARTIFACT_MCP_CONNECTOR_HERMETIC_CI_VAR_1().BASE_API_URL}/v1/mcp_servers?limit=1000\`; in that case use each entry's \`display_name\` as the \`server\` value (exact display names are always accepted alongside tool-prefix segments).
