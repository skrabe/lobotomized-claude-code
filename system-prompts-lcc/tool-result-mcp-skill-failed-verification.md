<!--
name: 'Tool result: MCP skill failed verification'
description: >-
  Error when an MCP skill failed verification and has no cached entry to
  refresh.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_0
  - TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_1
  - TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_2
  - TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_3
-->
${TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_0}, ${TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_1}. ${TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_2.includes("frontmatter")?"This is a problem with the server; retrying will not help until the server's owner fixes it.":TOOL_RESULT_MCP_SKILL_FAILED_VERIFICATION_VAR_3()}
