<!--
name: 'System Reminder: Subagent handback send enforce'
description: >-
  Meta reminder that forces a subagent to call SubagentHandback with its full
  report when requiresHandback is set and no report was delivered
ccVersion: 2.1.285
variables:
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_0
  - SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_1
-->
${SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_0} Your report has not been delivered. Call ${SYSTEM_REMINDER_SUBAGENT_HANDBACK_SEND_ENFORCE_VAR_1}({message: <your full report>}) now; the call ends your run.
