<!--
name: 'System Reminder: Dir Sync User Branch Followed'
description: >-
  Tells the cloud agent the checkout followed the user's branch (or detached
  HEAD), including any previous tip kept under a ref.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_2
-->
${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0(SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1.branch,SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1.agentCommits)}${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1.branch.previousTip===null?"":` This checkout's own branch of that name pointed at ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_2(SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1.branch.previousTip.tip)}, which the user's does not contain; that tip is kept at ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1.branch.previousTip.ref}.`}
