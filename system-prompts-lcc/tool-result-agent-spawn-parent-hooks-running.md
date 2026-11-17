<!--
name: 'Tool Result: Agent spawn refused, parent hooks still running'
description: >-
  Refuses spawning under a parent agent whose first turn.start hooks are still
  running and says to retry after they finish
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_AGENT_SPAWN_PARENT_HOOKS_RUNNING_VAR_0
-->
agent ${TOOL_RESULT_AGENT_SPAWN_PARENT_HOOKS_RUNNING_VAR_0} has not started its loop yet: its first turn.start hooks are still running. Try again after they finish, from outside those hooks.
