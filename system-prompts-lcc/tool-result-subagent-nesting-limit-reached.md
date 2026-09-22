<!--
name: 'Tool Result: Subagent nesting limit reached'
description: >-
  Error returned to the agent when it tries to spawn a subagent past the depth
  cap, telling it to complete the task directly
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_SUBAGENT_NESTING_LIMIT_REACHED_VAR_0
  - TOOL_RESULT_SUBAGENT_NESTING_LIMIT_REACHED_VAR_1
-->
Subagent nesting limit reached (depth ${TOOL_RESULT_SUBAGENT_NESTING_LIMIT_REACHED_VAR_0} of ${TOOL_RESULT_SUBAGENT_NESTING_LIMIT_REACHED_VAR_1}). Complete this task directly using your tools instead of spawning another agent. If the user explicitly requested deeper nesting, ask them to raise CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH.
