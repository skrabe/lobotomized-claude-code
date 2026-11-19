<!--
name: 'Status nudge: thread checklist/reply unchanged'
description: >-
  Periodic host status nudge for threaded hosts telling the model the thread's
  checklist or reply has not changed and to call the status tool with the
  current checklist.
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_STATUS_CHECK_THREAD_CHECKLIST_UNCHANGED_VAR_0
  - SYSTEM_REMINDER_STATUS_CHECK_THREAD_CHECKLIST_UNCHANGED_VAR_1
  - SYSTEM_REMINDER_STATUS_CHECK_THREAD_CHECKLIST_UNCHANGED_VAR_2
-->
Status check: this thread's checklist or reply has not changed for at least ${SYSTEM_REMINDER_STATUS_CHECK_THREAD_CHECKLIST_UNCHANGED_VAR_0/60} minutes. The user can only see what \`${SYSTEM_REMINDER_STATUS_CHECK_THREAD_CHECKLIST_UNCHANGED_VAR_1}\` and \`${SYSTEM_REMINDER_STATUS_CHECK_THREAD_CHECKLIST_UNCHANGED_VAR_2}\` post, and a thread that shows no change reads as stuck. Call \`${SYSTEM_REMINDER_STATUS_CHECK_THREAD_CHECKLIST_UNCHANGED_VAR_1}\` now with the checklist as it stands (✓ done, ✱ in progress, ○ not started), then continue the work.
