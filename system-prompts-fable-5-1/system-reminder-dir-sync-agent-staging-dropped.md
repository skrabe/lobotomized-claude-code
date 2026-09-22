<!--
name: 'System Reminder: Dir Sync Agent Staging Dropped'
description: >-
  Tells the cloud agent the index now mirrors the user's staging, so what it had
  staged is unstaged, with a conditional suffix for files that were removed or
  changed.
ccVersion: 2.1.280
variables:
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_DROPPED_VAR_0
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_DROPPED_VAR_1
  - SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_DROPPED_VAR_2
-->
The index now mirrors the user's staging; what you had staged in ${SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_DROPPED_VAR_0(SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_DROPPED_VAR_1)} is unstaged${SYSTEM_REMINDER_DIR_SYNC_AGENT_STAGING_DROPPED_VAR_2}.
