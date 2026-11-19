<!--
name: 'System Reminder: Cross-session remote delivery do not resend (still stored)'
description: >-
  Tells Claude not to resend because the remote session may still take the
  message after a restart, and to warn the user about duplicate work
ccVersion: 2.1.328
variables:
  - >-
    SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DO_NOT_RESEND_STILL_STORED_VAR_0
-->
Do not resend, even once that session accepts messages again: it may still take ${SYSTEM_REMINDER_CROSS_SESSION_REMOTE_DELIVERY_DO_NOT_RESEND_STILL_STORED_VAR_0} after a restart. Warn your user that a copy, or the same work done another way, may happen twice.
