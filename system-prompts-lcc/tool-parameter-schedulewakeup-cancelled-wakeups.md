<!--
name: 'Tool parameter: ScheduleWakeup cancelledWakeups result field'
description: >-
  Model-facing outputSchema field description on the ScheduleWakeup (/loop)
  tool, explaining how many pending dynamic-loop wakeups a stop:true call
  cancelled
ccVersion: 2.1.206
-->
How many pending dynamic-loop wakeups stop:true cancelled. 0 means nothing was pending — a recurring /loop cron is not cancelled by stop:true.
