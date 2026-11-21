<!--
name: 'System Reminder: Steward review skipped for ConfigChange hook'
description: >-
  Tells Claude to skip the unattended review because a ConfigChange hook could
  reload skills, and tell the user
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_STEWARD_REVIEW_SKIPPED_CONFIG_CHANGE_HOOK_VAR_0
-->
${SYSTEM_REMINDER_STEWARD_REVIEW_SKIPPED_CONFIG_CHANGE_HOOK_VAR_0==="set"?"a ConfigChange hook is set in this session":"a plugin's hooks are still loading, and one may be a ConfigChange hook"}, and the check ahead of an unattended review would reload the skills without asking it. Skip the review, go on with the rest, and tell the user that no review ran and why
