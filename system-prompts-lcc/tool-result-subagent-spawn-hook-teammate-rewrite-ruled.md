<!--
name: Teammate Spawn Rewrite Permission Refusal
description: >-
  Reports a plugin rewrite of a teammate spawn that a permission rule asks or
  denies.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_TEAMMATE_REWRITE_RULED_VAR_0
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_TEAMMATE_REWRITE_RULED_VAR_1
-->
A plugin's agent.spawn hook rewrote this spawn into one a permission rule ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_TEAMMATE_REWRITE_RULED_VAR_0[Z.behavior]}: ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_TEAMMATE_REWRITE_RULED_VAR_1.message} Dispatch it directly.
