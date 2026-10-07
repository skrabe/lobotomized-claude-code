<!--
name: 'Tool Result: Workflow agent spawn denied by plugin'
description: >-
  Error thrown from a workflow agent() call when a plugin's agent.spawn hook
  denies the spawn, carrying the plugin's deny reason.
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_WORKFLOW_AGENT_SPAWN_DENIED_BY_PLUGIN_VAR_0
-->
Workflow agent spawn denied by a plugin: ${TOOL_RESULT_WORKFLOW_AGENT_SPAWN_DENIED_BY_PLUGIN_VAR_0.deny}
