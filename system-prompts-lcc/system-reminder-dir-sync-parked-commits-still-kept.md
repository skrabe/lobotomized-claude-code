<!--
name: 'System Reminder: Directory sync parked commits still kept'
description: >-
  dir_sync_notice telling the model commits set aside earlier are still at named
  refs off the work branch and to merge or cherry-pick what it still needs.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_1
-->
Directory sync: commits of yours set aside at an earlier turn are still kept at ${SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_0.map(SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_1).join(", ")} (not on the work branch); merge or cherry-pick what you still need.
