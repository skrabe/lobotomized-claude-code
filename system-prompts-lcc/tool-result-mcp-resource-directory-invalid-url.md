<!--
name: 'Tool Result: MCP resource directory invalid URL'
description: >-
  Refusal to list a directory whose address is not a valid URL while a skill
  from this server is loaded
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_0
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_1
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_2
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_3
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_4
-->
${TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_0(TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_1)}: This directory was not read, because its address is not a valid URL. While a skill from this server is loaded, this app reads a directory only at a valid URL. Write the address as the server or the skill gives it.${TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_2.map((TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_3)=>TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_4(TOOL_RESULT_MCP_RESOURCE_DIRECTORY_INVALID_URL_VAR_3.skillName)).join("")}
