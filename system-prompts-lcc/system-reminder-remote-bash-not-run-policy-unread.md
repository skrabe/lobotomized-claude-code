<!--
name: 'System Reminder: Remote bash not run (policy unread)'
description: >-
  Tells that a '!' command did not run because the organization's settings could
  not be loaded, and asks to send it again
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_REMOTE_BASH_NOT_RUN_POLICY_UNREAD_VAR_0
  - SYSTEM_REMINDER_REMOTE_BASH_NOT_RUN_POLICY_UNREAD_VAR_1
-->
Not run: Claude couldn't load your organization's settings. Send it again. ${SYSTEM_REMINDER_REMOTE_BASH_NOT_RUN_POLICY_UNREAD_VAR_0(SYSTEM_REMINDER_REMOTE_BASH_NOT_RUN_POLICY_UNREAD_VAR_1)}
