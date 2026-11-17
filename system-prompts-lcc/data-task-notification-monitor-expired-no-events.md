<!--
name: 'Data: Monitor expired with no events notification'
description: >-
  Task notification that a Monitor expired with no events delivered, with re-arm
  advice and a hint to widen the filter
ccVersion: 2.1.326
variables:
  - DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_NO_EVENTS_VAR_0
  - DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_NO_EVENTS_VAR_1
  - DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_NO_EVENTS_VAR_2
-->
[Monitor expired after ${DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_NO_EVENTS_VAR_0} with no events delivered. ${DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_NO_EVENTS_VAR_1}${DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_NO_EVENTS_VAR_2} — and widen the filter if silence was unexpected.]
