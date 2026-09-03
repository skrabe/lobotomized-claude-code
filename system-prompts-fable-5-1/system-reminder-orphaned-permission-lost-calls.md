<!--
name: 'System Reminder: Orphaned Permission Lost Calls'
description: >-
  Meta command-queue value after a restart listing sibling tool calls whose
  results were lost, for the model to check before re-issuing.
ccVersion: 2.1.259
variables:
  - SYSTEM_REMINDER_ORPHANED_PERMISSION_LOST_CALLS_VAR_0
  - SYSTEM_REMINDER_ORPHANED_PERMISSION_LOST_CALLS_VAR_1
-->
This session restarted during your previous turn. Besides the tool calls answered above, that turn had also issued ${SYSTEM_REMINDER_ORPHANED_PERMISSION_LOST_CALLS_VAR_0===1?"a call whose result was":"calls whose results were"} lost to the restart: ${SYSTEM_REMINDER_ORPHANED_PERMISSION_LOST_CALLS_VAR_1.join(", ")} — ${SYSTEM_REMINDER_ORPHANED_PERMISSION_LOST_CALLS_VAR_0===1?"it":"they"} may not have run, or not completely. Check before issuing ${SYSTEM_REMINDER_ORPHANED_PERMISSION_LOST_CALLS_VAR_0===1?"it":"them"} again, and decide whether ${SYSTEM_REMINDER_ORPHANED_PERMISSION_LOST_CALLS_VAR_0===1?"it is":"they are"} still needed.
