<!--
name: 'System Reminder: Send-to-project create uncertain after interruption'
description: >-
  Task notification after an interrupted create call with no definite answer,
  telling the model to have the user check their Projects list before rerunning
  to avoid a duplicate.
ccVersion: 2.1.314
variables:
  - SYSTEM_REMINDER_SEND_TO_PROJECT_CREATE_UNCERTAIN_VAR_0
  - SYSTEM_REMINDER_SEND_TO_PROJECT_CREATE_UNCERTAIN_VAR_1
-->
The create call was cut off without a definite answer (${SYSTEM_REMINDER_SEND_TO_PROJECT_CREATE_UNCERTAIN_VAR_0(SYSTEM_REMINDER_SEND_TO_PROJECT_CREATE_UNCERTAIN_VAR_1.reason)}). Tell the user to check their Projects list on claude.ai/code before they run /send-to-project again, so they don’t end up with a duplicate.
