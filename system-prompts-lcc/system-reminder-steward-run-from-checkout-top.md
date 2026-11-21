<!--
name: 'System Reminder: Steward run from checkout top'
description: 'Reason gh and git must run in the checkout''s top folder, with the cd to use'
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_STEWARD_RUN_FROM_CHECKOUT_TOP_VAR_0
-->
gh and git, but for gh api, run only in the checkout's top folder (run cd '${SYSTEM_REMINDER_STEWARD_RUN_FROM_CHECKOUT_TOP_VAR_0}' in a call of its own first; if the shell doesn't stay there, start the line with: cd '${SYSTEM_REMINDER_STEWARD_RUN_FROM_CHECKOUT_TOP_VAR_0}' &&)
