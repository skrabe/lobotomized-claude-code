<!--
name: 'System Reminder: Subagent Handback Send Enforce'
description: >-
  Meta reminder that forces a subagent to call SubagentHandback with its full
  report when requiresHandback is set and no report was delivered.
ccVersion: 2.1.267
variables:
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_0
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_1
-->
${SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_0} Your report has not been delivered. Call ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_1}({message: <your full report>}) now, then stop.
