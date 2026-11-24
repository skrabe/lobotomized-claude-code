<!--
name: 'Skill: MCP address lookup needs approval'
description: Permission ask message for asking an MCP server for the skill at an address.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_SKILL_MCP_ADDRESS_ASK_APPROVAL_VAR_0
  - TOOL_RESULT_SKILL_MCP_ADDRESS_ASK_APPROVAL_VAR_1
-->
This asks an MCP server for the skill at an address, and ${TOOL_RESULT_SKILL_MCP_ADDRESS_ASK_APPROVAL_VAR_0===null?"a limit on that server needs an approval or could not be read":`an ask rule covers ${TOOL_RESULT_SKILL_MCP_ADDRESS_ASK_APPROVAL_VAR_1}`}, so a person must approve it.
