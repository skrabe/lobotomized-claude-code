<!--
name: 'Tool Result: Subagent Spawn Hook Rewrite Ruled'
description: >-
  Agent tool error returned when a plugin's agent.spawn hook rewrote a spawn
  into one that a permission rule asks for or denies. It tells Claude to
  dispatch the spawn directly.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_0
  - TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_1
-->
A plugin's agent.spawn hook rewrote this spawn into one a permission rule ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_0[st.behavior]}: ${TOOL_RESULT_SUBAGENT_SPAWN_HOOK_REWRITE_RULED_VAR_1.message} Dispatch it directly.
