<!--
name: 'Data: Loop wakeup expired on resume'
description: >-
  Reports how late the session restarted after a missed loop wakeup and that the
  loop remains stopped.
ccVersion: 2.1.295
variables:
  - DATA_TASK_NOTIFICATION_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_0
  - DATA_TASK_NOTIFICATION_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_1
-->
This session restarted ${DATA_TASK_NOTIFICATION_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_0<60000?"less than a minute":DATA_TASK_NOTIFICATION_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_1(DATA_TASK_NOTIFICATION_LOOP_WAKEUP_EXPIRED_ON_RESUME_VAR_0)} after its next /loop wakeup was due, so that wakeup will not fire. The loop stays stopped until Claude schedules it again: reply to continue it.
