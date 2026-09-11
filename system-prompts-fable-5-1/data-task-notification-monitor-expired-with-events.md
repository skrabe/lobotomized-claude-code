<!--
name: 'Data: Task Notification Monitor Expired With Events'
description: >-
  Housekeeping task notification telling the model a bounded monitor expired
  after delivering events and should be re-armed if still needed.
ccVersion: 2.1.268
variables:
  - DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_WITH_EVENTS_VAR_0
  - DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_WITH_EVENTS_VAR_1
  - DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_WITH_EVENTS_VAR_2
-->
[Monitor expired after ${DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_WITH_EVENTS_VAR_0} with ${DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_WITH_EVENTS_VAR_1} ${DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_WITH_EVENTS_VAR_2(DATA_TASK_NOTIFICATION_MONITOR_EXPIRED_WITH_EVENTS_VAR_1,"event")} delivered. Re-arm it if you still need the watch.]
