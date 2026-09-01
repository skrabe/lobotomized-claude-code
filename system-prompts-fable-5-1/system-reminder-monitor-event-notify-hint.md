<!--
name: Monitor event notification hint
description: >-
  Hint inside the monitor-event task-notification injected into agent context,
  telling it to send a notification only for user-actionable events.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_MONITOR_EVENT_NOTIFY_HINT_VAR_0
-->

If this event is something the user would act on now, send a ${SYSTEM_REMINDER_MONITOR_EVENT_NOTIFY_HINT_VAR_0}. Routine or benign output doesn't need one.
