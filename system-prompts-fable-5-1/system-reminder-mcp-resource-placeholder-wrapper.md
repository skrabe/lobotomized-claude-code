<!--
name: 'System Reminder: MCP resource placeholder wrapper'
description: >-
  Model-facing isMeta reminder emitted for an MCP resource that yielded nothing
  renderable: `<mcp-resource server=".." uri="..">(REASON)</mcp-resource>`,
  where REASON is "No content" or "No displayable content". Replaces the two
  per-reason ids catalogued through CC 2.1.233, which 2.1.234 collapsed into
  this single parameterized template.
ccVersion: 2.1.234
variables:
  - SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_0
  - SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_1
  - SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_2
-->
<mcp-resource server="${SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_0(SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_1.server)}" uri="${SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_0(SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_1.uri)}">(${SYSTEM_REMINDER_MCP_RESOURCE_PLACEHOLDER_WRAPPER_VAR_2})</mcp-resource>
