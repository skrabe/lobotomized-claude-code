<!--
name: 'System Reminder: Dir Sync Not Installed (Unlisted Reason)'
description: >-
  Tells the cloud agent that files it changed earlier are not on the user's
  machine as written and the truncated report gives no reason; the user's copies
  stand there while the checkout keeps the agent's changes.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_REASON_UNLISTED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_REASON_UNLISTED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_REASON_UNLISTED_VAR_2
-->
These files you changed earlier are not on the user's machine as you wrote them, and its report, cut short, does not say why; the user's own copies stand there (this checkout keeps your changes to them): ${SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_REASON_UNLISTED_VAR_0(SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_REASON_UNLISTED_VAR_1.map((SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_REASON_UNLISTED_VAR_2)=>SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_REASON_UNLISTED_VAR_2.path))}.
