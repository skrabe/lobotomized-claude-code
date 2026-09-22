<!--
name: 'Tool Result: Teammate Runtime Agent Type Cannot Run In Pane'
description: >-
  Subagent-launch error that a plugin-registered runtime agent type cannot run
  as a pane teammate and must be spawned with the named tool or in-process.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_TEAMMATE_RUNTIME_AGENT_TYPE_CANNOT_RUN_IN_PANE_VAR_0
  - TOOL_RESULT_TEAMMATE_RUNTIME_AGENT_TYPE_CANNOT_RUN_IN_PANE_VAR_1
-->
Agent type '${TOOL_RESULT_TEAMMATE_RUNTIME_AGENT_TYPE_CANNOT_RUN_IN_PANE_VAR_0.agent_type}' was registered at run time by a plugin and exists only in this process; a pane-based teammate cannot run it. Spawn it with the ${TOOL_RESULT_TEAMMATE_RUNTIME_AGENT_TYPE_CANNOT_RUN_IN_PANE_VAR_1} tool instead, or use in-process teammates.
