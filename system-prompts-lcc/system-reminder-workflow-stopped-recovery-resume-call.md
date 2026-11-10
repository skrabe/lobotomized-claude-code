<!--
name: 'System Reminder: Stopped workflow recovery resume call'
description: >-
  Recovery block saying finished agent calls are saved and giving the resume
  call to use only if the user asks
ccVersion: 2.1.322
variables:
  - SYSTEM_REMINDER_WORKFLOW_STOPPED_RECOVERY_RESUME_CALL_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_STOPPED_RECOVERY_RESUME_CALL_VAR_1
  - SYSTEM_REMINDER_WORKFLOW_STOPPED_RECOVERY_RESUME_CALL_VAR_2
-->

<recovery>${SYSTEM_REMINDER_WORKFLOW_STOPPED_RECOVERY_RESUME_CALL_VAR_0(`Its finished agent calls are saved. Only if the user asks you to resume it, call: ${SYSTEM_REMINDER_WORKFLOW_STOPPED_RECOVERY_RESUME_CALL_VAR_1(SYSTEM_REMINDER_WORKFLOW_STOPPED_RECOVERY_RESUME_CALL_VAR_2)}`)}</recovery>
