<!--
name: 'System Reminder: Cross-Session Idle Notice Exited'
description: >-
  Meta prompt injected when a subscribed peer exits before going idle, telling
  the model that address will not process further messages.
ccVersion: 2.1.237
variables:
  - SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_0
  - SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_1
  - SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_2
-->
[Cross-session idle notice] "${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_0.label}", which you asked to be notified about, has exited${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_0.finishedAt!==void 0?` (at ${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_1(SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_0.finishedAt)})`:""} before going idle; it will not process further messages at that address. ${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_EXITED_VAR_2}
