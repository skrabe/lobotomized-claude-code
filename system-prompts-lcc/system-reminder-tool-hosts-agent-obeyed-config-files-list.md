<!--
name: 'Tool Hosts Notice: Agent-Obeyed Config Files List'
description: >-
  Fragment listing the files the user's Claude Code or git obeys (.claude
  directory, .mcp.json, CLAUDE.md, AGENTS.md, .gitattributes …), interpolated
  into the moving-work-between-copies guidance.
ccVersion: 2.1.277
variables:
  - SYSTEM_REMINDER_TOOL_HOSTS_AGENT_OBEYED_CONFIG_FILES_LIST_VAR_0
  - SYSTEM_REMINDER_TOOL_HOSTS_AGENT_OBEYED_CONFIG_FILES_LIST_VAR_1
-->
a ${SYSTEM_REMINDER_TOOL_HOSTS_AGENT_OBEYED_CONFIG_FILES_LIST_VAR_0} directory, ${SYSTEM_REMINDER_TOOL_HOSTS_AGENT_OBEYED_CONFIG_FILES_LIST_VAR_1.slice(0,-1).join(", ")} and ${SYSTEM_REMINDER_TOOL_HOSTS_AGENT_OBEYED_CONFIG_FILES_LIST_VAR_1.at(-1)}
