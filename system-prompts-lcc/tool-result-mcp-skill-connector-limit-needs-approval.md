<!--
name: 'Tool result: MCP skill connector limit needs approval'
description: >-
  Skill not loaded because its connector limit now asks for approval or could
  not be read; retry once, then stop.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_CONNECTOR_LIMIT_NEEDS_APPROVAL_VAR_0
  - TOOL_RESULT_MCP_SKILL_CONNECTOR_LIMIT_NEEDS_APPROVAL_VAR_1
-->
The skill "${TOOL_RESULT_MCP_SKILL_CONNECTOR_LIMIT_NEEDS_APPROVAL_VAR_0}" was not loaded, because its connector's limit asks for an approval now, or could not be read. Use the ${TOOL_RESULT_MCP_SKILL_CONNECTOR_LIMIT_NEEDS_APPROVAL_VAR_1} tool once more. If the skill is refused again, stop and tell the user.
