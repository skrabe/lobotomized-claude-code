<!--
name: 'Tool result: MCP skill safety scan cannot take it'
description: >-
  Error when the safety scan cannot take an MCP skill because of size or file
  types.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_SKILL_SAFETY_SCAN_CANNOT_TAKE_VAR_0
  - TOOL_RESULT_MCP_SKILL_SAFETY_SCAN_CANNOT_TAKE_VAR_1
  - TOOL_RESULT_MCP_SKILL_SAFETY_SCAN_CANNOT_TAKE_VAR_2
-->
${TOOL_RESULT_MCP_SKILL_SAFETY_SCAN_CANNOT_TAKE_VAR_0}, because Anthropic's safety scan cannot take it. ${TOOL_RESULT_MCP_SKILL_SAFETY_SCAN_CANNOT_TAKE_VAR_1?"A file or the skill is too large, or it has an archive or binary file":`The scan takes at most ${TOOL_RESULT_MCP_SKILL_SAFETY_SCAN_CANNOT_TAKE_VAR_2[1]} in a text file and about ${TOOL_RESULT_MCP_SKILL_SAFETY_SCAN_CANNOT_TAKE_VAR_2[2]} in a skill, with its file names, and no archive or binary file`}. Do not repeat it. Tell the server's owner.
