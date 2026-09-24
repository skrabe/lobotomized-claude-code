<!--
name: 'System Reminder: Dir Sync Not Installed Stale Basis'
description: >-
  Tells the cloud agent some files are not yet written on the user's machine
  because the copy sent predated the user's latest changes; sync resolves it
  with no action needed.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_STALE_BASIS_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_STALE_BASIS_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_STALE_BASIS_VAR_2
-->
Not written on the user's machine yet, because the copy sent there was made before the user's latest changes to them reached this checkout: ${SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_STALE_BASIS_VAR_0(SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_STALE_BASIS_VAR_1.map((SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_STALE_BASIS_VAR_2)=>SYSTEM_REMINDER_DIR_SYNC_NOT_INSTALLED_STALE_BASIS_VAR_2.path))} — sync settles this by itself; nothing for you to do.
