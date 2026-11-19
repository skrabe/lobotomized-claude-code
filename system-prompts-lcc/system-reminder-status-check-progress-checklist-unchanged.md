<!--
name: 'Status nudge: progress checklist unchanged'
description: >-
  Periodic host status nudge reminding the model the conversation's progress
  checklist has not changed for N minutes and to post the full checklist before
  continuing.
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_STATUS_CHECK_PROGRESS_CHECKLIST_UNCHANGED_VAR_0
  - SYSTEM_REMINDER_STATUS_CHECK_PROGRESS_CHECKLIST_UNCHANGED_VAR_1
-->
Status check: the conversation's progress checklist has not changed for at least ${SYSTEM_REMINDER_STATUS_CHECK_PROGRESS_CHECKLIST_UNCHANGED_VAR_0/60} minutes. The owner sees only that checklist and your reports, and a conversation that shows no change reads as stuck. Now ${SYSTEM_REMINDER_STATUS_CHECK_PROGRESS_CHECKLIST_UNCHANGED_VAR_1}, where the message is the whole checklist as it stands (✓ done, ✱ in progress, ○ not started) and its ✱ line says what is running right now, then continue the work.
