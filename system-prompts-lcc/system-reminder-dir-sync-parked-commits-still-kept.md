<!--
name: 'System Reminder: Directory sync parked commits still kept'
description: >-
  dir_sync_notice telling the model commits set aside earlier are still kept at
  named refs off the work branch, to merge or cherry-pick back only what is its
  own and still wanted, and never commits a remote already has.
ccVersion: 2.1.281
variables:
  - SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_1
-->
Directory sync: commits set aside at an earlier turn are still kept at ${SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_0.map(SYSTEM_REMINDER_DIR_SYNC_PARKED_COMMITS_STILL_KEPT_VAR_1).join(", ")} (not on the work branch); merge or cherry-pick back only what is yours and still wanted — nothing a remote already has (\`git branch -r --contains COMMIT\` lists the remote branches holding one).
