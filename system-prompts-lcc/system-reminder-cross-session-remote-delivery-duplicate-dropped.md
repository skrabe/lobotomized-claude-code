<!--
name: 'System Reminder: Cross-session remote delivery duplicate dropped'
description: >-
  Tells Claude the remote session dropped a repeat and when it may resend based
  on the earlier copy's notice
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_0
  - SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_1
  - SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_2
  - SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_3
-->
${SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_0} It dropped this repeat, which does not show what became of the earlier copy. Do not resend unless the latest notice about the earlier copy said that it was not delivered, and named no way for it to be delivered later.${SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_1?" That session may still take the repeat after a restart.":""}${SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_2?` ${SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DUPLICATE_DROPPED_VAR_3}`:""}
