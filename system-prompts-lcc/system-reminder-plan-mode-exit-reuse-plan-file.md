<!--
name: 'System Reminder: Plan mode exit reuse plan file'
description: >-
  After exiting plan mode, tells Claude this is the one plan file the user sees
  and to re-enter plan mode and overwrite it for a different plan
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_PLAN_MODE_EXIT_REUSE_PLAN_FILE_VAR_0
-->
 It is the one plan file the user is shown. If the user later asks for a plan of different work, call ${SYSTEM_REMINDER_PLAN_MODE_EXIT_REUSE_PLAN_FILE_VAR_0} first and overwrite this file with the new plan, so that they can read and approve it.
