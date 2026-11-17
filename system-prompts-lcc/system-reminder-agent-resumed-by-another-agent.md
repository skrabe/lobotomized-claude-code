<!--
name: 'System reminder: agent resumed by another agent'
description: >-
  Notice to the parent that its waiting background agent was resumed by another
  agent and now reports there.
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_AGENT_RESUMED_BY_ANOTHER_AGENT_VAR_0
  - SYSTEM_REMINDER_AGENT_RESUMED_BY_ANOTHER_AGENT_VAR_1
-->
Agent "${SYSTEM_REMINDER_AGENT_RESUMED_BY_ANOTHER_AGENT_VAR_0.description}", which was waiting on its own background work, was resumed by another agent (${SYSTEM_REMINDER_AGENT_RESUMED_BY_ANOTHER_AGENT_VAR_1}) and now reports to that agent. Do not treat its work as cancelled or relaunch it, and do not count on a notification from it here, even after messaging it.
