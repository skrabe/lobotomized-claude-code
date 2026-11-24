<!--
name: 'Tool Result: MCP skill server limit asks approval'
description: >-
  Skill load result when a server limit needs approval or is unreadable, telling
  the model to retry once then stop
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_MCP_SKILL_SERVER_LIMIT_ASK_RETRY_VAR_0
  - TOOL_RESULT_MCP_SKILL_SERVER_LIMIT_ASK_RETRY_VAR_1
-->
${TOOL_RESULT_MCP_SKILL_SERVER_LIMIT_ASK_RETRY_VAR_0}: that server's limit asks for an approval now, or could not be read. Use the ${TOOL_RESULT_MCP_SKILL_SERVER_LIMIT_ASK_RETRY_VAR_1} tool once more. If it is refused again, stop and tell the user.
