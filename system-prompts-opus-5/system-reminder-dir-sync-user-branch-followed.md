<!--
name: 'System Reminder: Dir Sync User Branch Followed'
description: >-
  Tells the cloud agent the checkout followed the user's branch (or detached
  HEAD), including any previous tip kept under a ref.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_2
-->
The user is ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0.branch.to===null?"on a detached HEAD":`on branch ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0.branch.to)}`}; this checkout followed (it was ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0.branch.from===null?"detached":`on ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_1(SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0.branch.from)}`}, which stays where it was).${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0.branch.previousTip===null?"":` This checkout's own branch of that name pointed at ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_2(SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0.branch.previousTip.tip)}, which the user's does not contain; that tip is kept at ${SYSTEM_REMINDER_DIR_SYNC_USER_BRANCH_FOLLOWED_VAR_0.branch.previousTip.ref}.`}
