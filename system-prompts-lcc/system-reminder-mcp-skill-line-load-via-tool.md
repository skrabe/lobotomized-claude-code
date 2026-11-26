<!--
name: 'System reminder: possible MCP skill line'
description: >-
  Meta message added when a typed line may name an MCP server skill that has not
  loaded, telling Claude to load it via the skill tool and not do its work
  another way.
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_MCP_SKILL_LINE_LOAD_VIA_TOOL_VAR_0
-->
This line possibly names a skill of an MCP server. No skill has loaded: the skill may need the user's approval, or its server is still connecting. To load it, call the ${SYSTEM_REMINDER_MCP_SKILL_LINE_LOAD_VIA_TOOL_VAR_0} tool with the name and the arguments in the line. If the call is refused, do not do the skill's work another way.
