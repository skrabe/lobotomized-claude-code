<!--
name: 'Tool result: subagent spawn hook required MCP missing'
description: >-
  Agent tool error when an agent named by a plugin's agent.spawn hook requires
  MCP servers that have no tools yet.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_0
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_1
-->
Agent '${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_0}', named by a plugin's agent.spawn hook, requires MCP servers matching: ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_1.join(", ")}; none has tools yet. Use /mcp to configure and authenticate them.
