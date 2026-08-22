<!--
name: 'Data: Artifact MCP connector guidance'
description: >-
  Explains how Artifact MCP manifests declare claude.ai, built-in, and host
  connectors and how to discover exact server and upstream tool names
ccVersion: 2.1.239
variables:
  - CONNECTOR_TOOL_GUIDANCE
  - BUILT_IN_CONNECTOR_GUIDANCE
  - HOST_MCP_SERVER_GUIDANCE
  - MCP_SERVERS_BETA_DESCRIPTOR
  - API_CONFIG_FN
-->
${CONNECTOR_TOOL_GUIDANCE}${BUILT_IN_CONNECTOR_GUIDANCE}${HOST_MCP_SERVER_GUIDANCE} The manifest's \`tools\` array takes the connector's upstream tool names (as returned by \`listTools()\` / \`/v1/mcp_servers\`), which can differ from the normalized \`<toolName>\` segment when an upstream name contains \`.\` or spaces. In hermetic/CI sessions where connectors aren't loaded but \`$CLAUDE_CODE_OAUTH_TOKEN\` is set, fetch the list via Bash: \`curl -H 'anthropic-version: 2023-06-01' -H 'anthropic-beta: ${MCP_SERVERS_BETA_DESCRIPTOR.header}' -H "Authorization: Bearer $CLAUDE_CODE_OAUTH_TOKEN" ${API_CONFIG_FN().BASE_API_URL}/v1/mcp_servers?limit=1000\`; in that case use each entry's \`display_name\` as the \`server\` value (exact display names are always accepted alongside tool-prefix segments).
