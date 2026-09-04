<!--
name: Subagent Spawn Hook Mcp Required Missing
description: >-
  Agent-tool error when a hook-selected agent requires MCP servers that still
  have no tools.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_0
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_1
-->
Agent '${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_0.agentType}', named by a plugin's agent.spawn hook, requires MCP servers matching: ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_MCP_REQUIRED_MISSING_VAR_1.join(", ")}; none has tools yet. Use /mcp to configure and authenticate them.
