<!--
name: 'Tool Result: Subagent spawn hook rewrite ruled'
description: >-
  Agent tool error when a plugin agent.spawn hook rewrote the spawn into one a
  permission rule denies or asks about, telling the model to dispatch it
  directly.
ccVersion: 2.1.296
variables:
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_0
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_1
-->
A plugin's agent.spawn hook rewrote this spawn into one a permission rule ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_0[St.behavior]}: ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_1.message} Dispatch it directly.
