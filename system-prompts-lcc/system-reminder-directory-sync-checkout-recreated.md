<!--
name: 'System Reminder: Directory Sync Checkout Recreated'
description: >-
  Reminds the model that the cloud checkout was recreated from starting state
  and earlier-turn files are not present yet.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_CHECKOUT_RECREATED_VAR_0
  - SYSTEM_REMINDER_DIRECTORY_SYNC_CHECKOUT_RECREATED_VAR_1
-->
Directory sync: this checkout was RECREATED from the session's starting state (the cloud container was replaced), and the earlier environment's work could not be restored here (${SYSTEM_REMINDER_DIRECTORY_SYNC_CHECKOUT_RECREATED_VAR_0.agent}). Commits and files from the earlier environment's turns are NOT here, and ${SYSTEM_REMINDER_DIRECTORY_SYNC_CHECKOUT_RECREATED_VAR_1}
