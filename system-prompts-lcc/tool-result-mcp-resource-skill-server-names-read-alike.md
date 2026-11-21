<!--
name: 'Tool Result: MCP skill server names read alike'
description: >-
  Tail of the refused-read message when similar-looking server names are
  involved
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MCP_RESOURCE_SKILL_SERVER_NAMES_READ_ALIKE_VAR_0
  - TOOL_RESULT_MCP_RESOURCE_SKILL_SERVER_NAMES_READ_ALIKE_VAR_1
  - TOOL_RESULT_MCP_RESOURCE_SKILL_SERVER_NAMES_READ_ALIKE_VAR_2
-->
${TOOL_RESULT_MCP_RESOURCE_SKILL_SERVER_NAMES_READ_ALIKE_VAR_0}, and these server names read alike. ${TOOL_RESULT_MCP_RESOURCE_SKILL_SERVER_NAMES_READ_ALIKE_VAR_1.length<TOOL_RESULT_MCP_RESOURCE_SKILL_SERVER_NAMES_READ_ALIKE_VAR_2.length?"A loaded skill of this server has the address too. While these skills are loaded, this address is not read from any of these servers.":"To read a file of that skill, give its server's exact name. If this call gave that name, no server has that name now."}
