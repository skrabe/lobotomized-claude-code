<!--
name: 'Schedule Note: Local MCP Not Attachable To Routines'
description: >-
  Setup note that locally configured MCP servers cannot be attached to cloud
  routines, which can only use claude.ai connectors.
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_0
  - SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_1
  - SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_2
-->
No MCP connectors for cloud scheduled tasks, which can only use claude.ai connectors. ${SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_0} MCP ${SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_1(SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_0,"server")} configured in Claude Code can't be attached (run /mcp to see ${SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_1(SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_0,"it","them")}). ${SLASH_COMMAND_SCHEDULE_NOTE_LOCAL_MCP_NOT_ATTACHABLE_VAR_2}
