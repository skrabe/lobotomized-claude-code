<!--
name: Background agent not-resumed notice
description: >-
  Task-notification injected to the model that a checkpointed agent was not
  resumed.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_BACKGROUND_AGENT_NOT_RESUMED_VAR_0
  - SYSTEM_REMINDER_BACKGROUND_AGENT_NOT_RESUMED_VAR_1
-->
Background agent "${SYSTEM_REMINDER_BACKGROUND_AGENT_NOT_RESUMED_VAR_0(SYSTEM_REMINDER_BACKGROUND_AGENT_NOT_RESUMED_VAR_1.description)}" was checkpointed for the background fork but the fork failed to spawn; the agent was not resumed.
