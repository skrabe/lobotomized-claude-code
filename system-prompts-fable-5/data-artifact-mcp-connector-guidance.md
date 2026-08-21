<!--
name: 'Data: Artifact MCP connector guidance'
description: >-
  Explains how Artifact MCP manifests identify claude.ai connectors and discover
  upstream tool names; injected into the Artifact capabilities skill.
ccVersion: 2.1.238
variables:
  - GET_CLAUDEAI_CONNECTORS_FN
  - TOOLS
  - HAS_HOST_MCP_SERVER_SUPPORT
  - MCP_SERVERS_BETA_DESCRIPTOR
  - API_CONFIG_FN
-->
${GET_CLAUDEAI_CONNECTORS_FN(TOOLS).length>0?"Connector tools appear in your tool list as `mcp__<connector>__<toolName>`. Set `server` to the `<connector>` segment — everything between `mcp__` and the next `__` (for `mcp__claude_ai_Slack_beta__search`, the `server` is `claude_ai_Slack_beta`). Copy the segment exactly, case included; when publishing, it is resolved to the connector's display name automatically.":"None are connected right now — they may still be connecting, or the user has none. Look for tools prefixed `mcp__claude_ai_*` in your tool list; each is named `mcp__claude_ai_<connector>__<tool>`."} ${HAS_HOST_MCP_SERVER_SUPPORT?"Locally-configured MCP servers connected in this session can also be declared, as host servers: set `server` to `host:<server>` where `<server>` is the segment between `mcp__` and the next `__` in that server's tool names (`mcp__filesystem__read_file` → `host:filesystem`). A host server only answers when the viewer opens the page in a Claude app that has that same local server connected — say so to the user when you publish.":"Only claude.ai connectors are valid — locally-configured MCP servers are not."} The manifest's \`tools\` array takes the connector's upstream tool names (as returned by \`listTools()\` / \`/v1/mcp_servers\`), which can differ from the normalized \`<toolName>\` segment when an upstream name contains \`.\` or spaces. In hermetic/CI sessions where connectors aren't loaded but \`$CLAUDE_CODE_OAUTH_TOKEN\` is set, fetch the list via Bash: \`curl -H 'anthropic-version: 2023-06-01' -H 'anthropic-beta: ${MCP_SERVERS_BETA_DESCRIPTOR.header}' -H "Authorization: Bearer $CLAUDE_CODE_OAUTH_TOKEN" ${API_CONFIG_FN().BASE_API_URL}/v1/mcp_servers?limit=1000\`; in that case use each entry's \`display_name\` as the \`server\` value (exact display names are always accepted alongside tool-prefix segments).
