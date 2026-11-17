<!--
name: 'Slash command: skills unused MCP'
description: >-
  Skills usage report warning that MCP skills were loaded but never used, and
  that disabling the server also removes its tools.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_0
  - SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_1
  - SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_2
  - SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_3
-->
${SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_0.length} MCP ${SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_1(SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_0.length,"skill")} loaded but never used${SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_2}. Each one adds to the system prompt every turn. MCP skills live on the server, not on disk — turning ${SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_3?"that server":"those servers"} off in /mcp also removes ${SLASH_COMMAND_SKILLS_UNUSED_MCP_VAR_3?"its":"their"} tools.
