<!--
name: 'System Reminder: Directory Sync Missing History'
description: >-
  Reminds the model that the user's latest changes could not be applied because
  this checkout does not hold the required history object.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_MISSING_HISTORY_VAR_0
-->
Directory sync: the user's latest changes could not be brought into this checkout (they build on ${SYSTEM_REMINDER_DIRECTORY_SYNC_MISSING_HISTORY_VAR_0===null?"an object":`commit ${SYSTEM_REMINDER_DIRECTORY_SYNC_MISSING_HISTORY_VAR_0.slice(0,12)}`}, which this checkout does not hold — history below a shallow clone, or sync state lost with a replaced container); the user's machine has been asked to resend them on a base held here. The checkout is unchanged.
