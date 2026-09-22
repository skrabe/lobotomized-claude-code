<!--
name: 'System Reminder: Dir Sync Changed During Read'
description: >-
  Reminds the model that files still being written this turn were not sent to
  the user's machine.
ccVersion: 2.1.261
variables:
  - SYSTEM_REMINDER_DIR_SYNC_CHANGED_DURING_READ_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_CHANGED_DURING_READ_VAR_1
-->
Directory sync: these files were being written while this turn's files were read, so this turn's version of them was NOT sent to the user's machine (it keeps what it last had there): ${SYSTEM_REMINDER_DIR_SYNC_CHANGED_DURING_READ_VAR_0}${SYSTEM_REMINDER_DIR_SYNC_CHANGED_DURING_READ_VAR_1}. They go out at the next sync point that finds them at rest; if a process of yours keeps writing them, say so rather than report them delivered.
