<!--
name: 'System Reminder: Dir Sync Checkout Back On User Branch'
description: >-
  Agent-moved arm of the user-branch-followed reminder: this checkout is back on
  the user's HEAD or branch, which it follows at every turn.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_2
  - SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_3
-->
This checkout is back on the user's ${SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_0.to===null?"HEAD (detached)":SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_1}, which it follows at every turn (you had ${SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_0.from===null?"detached HEAD":`switched to ${SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_2(SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_0.from)}, which stays where it was`}).${SYSTEM_REMINDER_DIR_SYNC_CHECKOUT_BACK_ON_USER_BRANCH_VAR_3}
