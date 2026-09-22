<!--
name: Background agent resume-failed notice
description: >-
  Task-notification injected to the model that a checkpointed agent could not be
  resumed.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_0
  - SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_1
  - SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_2
-->
Background agent "${SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_0(SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_1.description??SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_1.agentId)}" was checkpointed for the background fork but could not be resumed (${SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_0(SYSTEM_REMINDER_BACKGROUND_AGENT_RESUME_FAILED_VAR_2)}).
