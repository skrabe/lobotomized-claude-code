<!--
name: 'System Reminder: Dir Sync Parked Reason Published'
description: >-
  Reason phrase interpolated into the parked-commits notice when some or all of
  the agent's commits are already on a remote and so are not re-created on the
  user's HEAD.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_PARKED_REASON_PUBLISHED_VAR_0
-->
${SYSTEM_REMINDER_DIR_SYNC_PARKED_REASON_PUBLISHED_VAR_0===0?"some":SYSTEM_REMINDER_DIR_SYNC_PARKED_REASON_PUBLISHED_VAR_0} of them are already on a remote (a remote-tracking ref has them: fetched, pulled, merged or rebased from it, or pushed) and a run that includes commits a remote already has is not re-created on the user's HEAD
