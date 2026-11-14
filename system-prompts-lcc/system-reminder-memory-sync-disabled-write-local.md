<!--
name: 'System Reminder: Memory sync disabled, write local'
description: >-
  Warns that memory sync is off for a reason, so the write is saved only on this
  machine and may upload later if policy allows, or is lost
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_MEMORY_SYNC_DISABLED_WRITE_LOCAL_VAR_0
-->
${SYSTEM_REMINDER_MEMORY_SYNC_DISABLED_WRITE_LOCAL_VAR_0} This write was saved on this machine only and is NOT being synced. It may be uploaded later from this machine if the policy then allows sync. If this machine is discarded first, as when a cloud session ends, it is lost.
