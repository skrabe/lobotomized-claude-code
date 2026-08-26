<!--
name: 'Data: Artifact MCP valid servers — meta plus no app or local'
description: >-
  Valid-`server` branch when a meta connector exists, allowing claude.ai
  connectors plus that meta server and excluding the Claude app's own servers
  and local MCP servers.
ccVersion: 2.1.246
variables:
  - DATA_ARTIFACT_MCP_CONNECTOR_VALID_SERVERS_PLUS_META_NO_APP_OR_LOCAL_VAR_0
-->
 Only claude.ai connectors and \`${DATA_ARTIFACT_MCP_CONNECTOR_VALID_SERVERS_PLUS_META_NO_APP_OR_LOCAL_VAR_0.server}\` are valid \`server\` values — the Claude app's own servers (\`cowork\`, \`workspace\`, \`scheduled-tasks\`, \`session_info\` and the like) and other locally-configured MCP servers in your tool list are not.
