<!--
name: 'System Reminder: Cross-Session Idle Notice Idle'
description: >-
  Meta prompt injected when a subscribed peer session goes idle, telling the
  model the named session is idle and to treat the notice as harness automation.
ccVersion: 2.1.237
variables:
  - SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_0
  - SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_1
  - SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_2
-->
[Cross-session idle notice] "${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_0.label}", which you asked to be notified about, is idle now${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_1?` — it finished a turn at ${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_1}`:""}.${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_0.detail?` Its harness reports: «${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_0.detail}».`:""} ${SYSTEM_REMINDER_CROSS_SESSION_IDLE_NOTICE_IDLE_VAR_2}
