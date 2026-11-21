<!--
name: 'Tool Result: Skill MCP version and source'
description: >-
  States the MCP skill's version and which server or connector it comes from in
  the skill load approval request
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_0
  - TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_1
  - TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_2
-->
Its version is ${TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_0(TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_1.version)} and it comes from ${TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_2(TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_1.serverName,TOOL_RESULT_SKILL_MCP_VERSION_AND_SOURCE_VAR_1.isConnector)}.
