<!--
name: 'System Reminder: Stopped agents resumed automatically'
description: Tells the model stopped agents are being resumed and will report back
ccVersion: 2.1.322
variables:
  - SYSTEM_REMINDER_STOPPED_AGENTS_RESUMED_AUTOMATICALLY_VAR_0
  - SYSTEM_REMINDER_STOPPED_AGENTS_RESUMED_AUTOMATICALLY_VAR_1
  - SYSTEM_REMINDER_STOPPED_AGENTS_RESUMED_AUTOMATICALLY_VAR_2
-->
These stopped agents are being resumed automatically from their saved transcripts: ${SYSTEM_REMINDER_STOPPED_AGENTS_RESUMED_AUTOMATICALLY_VAR_0.join(", ")}. Each goes on where it stopped and reports back to you in a notification when it is done, so do not start its task again unless the user asks for that.${SYSTEM_REMINDER_STOPPED_AGENTS_RESUMED_AUTOMATICALLY_VAR_1(SYSTEM_REMINDER_STOPPED_AGENTS_RESUMED_AUTOMATICALLY_VAR_2)?` If one does not report back, send a message to its agent id with the ${SYSTEM_REMINDER_STOPPED_AGENTS_RESUMED_AUTOMATICALLY_VAR_2} tool to resume it.`:""}
