<!--
name: 'System Reminder: Dir Sync Staged Files Gone'
description: >-
  Suffix on the staging-dropped reminder when every path the agent had staged is
  no longer in the checkout.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_NO_LONGER_IN_CHECKOUT_VAR_0
-->
 (${SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_NO_LONGER_IN_CHECKOUT_VAR_0?"that file is":"those files are"} no longer in the checkout)
