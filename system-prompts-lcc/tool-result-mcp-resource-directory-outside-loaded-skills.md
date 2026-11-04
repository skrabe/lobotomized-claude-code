<!--
name: 'Tool Result: MCP resource directory outside loaded skills'
description: >-
  Refuses an MCP resource directory read whose address lies outside the loaded
  skills' directories and explains how to copy the exact skill address or load
  the skill first
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_0
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_1
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_2
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_3
  - TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_4
-->
${TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_0(TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_1)}: This directory was not read, because its address, as written, is outside the directories of the loaded skills of this server. While a skill from this server is loaded, this tool reads, for this server, only the directories of its loaded skills. For a directory of a loaded skill, copy the address after "at" in that skill's first sentence, character for character, without the full stop. Add "/" and a path only for a subdirectory. If this conversation does not hold that sentence, load that skill here: its first sentence then gives the address. To read a directory of another skill of this server, load that skill first.${TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_2.map((TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_3)=>TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_4(TOOL_RESULT_MCP_RESOURCE_DIRECTORY_OUTSIDE_LOADED_SKILLS_VAR_3.skillName)).join("")}
