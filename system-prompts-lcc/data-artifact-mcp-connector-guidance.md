<!--
name: 'Data: Artifact MCP connector guidance'
description: >-
  Explains how Artifact MCP manifests declare claude.ai, built-in, and host
  connectors and how to discover exact server and upstream tool names
ccVersion: 2.1.246
variables:
  - CONNECTOR_SERVER_NAMING_GUIDANCE
  - HOSTED_CONNECTOR_RESOLUTION_GUIDANCE
  - BUILT_IN_META_CONNECTOR_GUIDANCE
  - HOST_MCP_SERVER_GUIDANCE
  - CONNECTOR_TOOL_DISCOVERY_SOURCE
  - HERMETIC_CONNECTOR_FALLBACK_GUIDANCE
-->
${CONNECTOR_SERVER_NAMING_GUIDANCE}${HOSTED_CONNECTOR_RESOLUTION_GUIDANCE}${BUILT_IN_META_CONNECTOR_GUIDANCE}${HOST_MCP_SERVER_GUIDANCE} The manifest's \`tools\` array takes the connector's upstream tool names (as returned by ${CONNECTOR_TOOL_DISCOVERY_SOURCE}), which can differ from the normalized \`<toolName>\` segment when an upstream name contains \`.\` or spaces. Every \`servers[]\` entry needs a non-empty \`tools\` array naming the tools the page calls — an empty or omitted \`tools\` list is refused and never means "all tools"; to publish without connector access, leave \`mcp\` out of \`capabilities\` (pass \`capabilities: {}\` to clear a stored declaration) rather than declaring an empty \`servers\` list.${HERMETIC_CONNECTOR_FALLBACK_GUIDANCE}
