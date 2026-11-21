<!--
name: 'Tool result: MCP skill needs approval'
description: >-
  Ask message for an MCP skill needing approval: a person approves it in an
  interactive session; don't approve it yourself.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_0
  - TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_1
  - TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_4
  - TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_2
  - TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_3
-->
${TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_0(TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_1.name,{...TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_4,isChanged:!1})} This skill needs approval before it loads. A person can approve it in an interactive Claude Code session, where the permission dialog names the skill${TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_2===null?"":` and its ${TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_3(TOOL_RESULT_MCP_SKILL_NEEDS_APPROVAL_ASK_VAR_4.isConnector)}`}. Do not try to approve it yourself.
