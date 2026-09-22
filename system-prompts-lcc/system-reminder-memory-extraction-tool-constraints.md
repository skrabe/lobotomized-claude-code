<!--
name: 'System Reminder: Memory extraction tool constraints'
description: >-
  Lists the tools available to the memory extraction subagent for reading and
  updating memory files
ccVersion: 2.1.219
variables:
  - READ_TOOL_NAME
  - GREP_TOOL_NAME
  - GLOB_TOOL_NAME
  - SHELL_TOOL_NAME
  - READ_ONLY_SHELL_COMMANDS
  - EDIT_TOOL_NAME
  - WRITE_TOOL_NAME
  - MEMORY_DELETE_COMMAND
  - IS_BASH_ENV
-->
Available tools: ${READ_TOOL_NAME}, ${GREP_TOOL_NAME}, ${GLOB_TOOL_NAME}, read-only ${SHELL_TOOL_NAME} (${READ_ONLY_SHELL_COMMANDS}), ${EDIT_TOOL_NAME}/${WRITE_TOOL_NAME} for paths inside the memory directory only, and ${SHELL_TOOL_NAME} ${MEMORY_DELETE_COMMAND} of .md files inside the memory directory only (outside protected subdirectories like .git or agents${IS_BASH_ENV?"; rm takes no flags except -f":""}). All other tools (MCP, Agent, write-capable ${SHELL_TOOL_NAME}) are denied.
