<!--
name: 'Data: Monitor timed out notification (likely stopped after reply)'
description: >-
  Task notification when a monitor timed out in a session where processes are
  likely stopped after the reply, telling the model to re-arm only if it has
  more to do before replying.
ccVersion: 2.1.326
variables:
  - DATA_TASK_NOTIFICATION_MONITOR_TIMED_OUT_LIKELY_STOPPED_AFTER_REPLY_VAR_0
-->
[${DATA_TASK_NOTIFICATION_MONITOR_TIMED_OUT_LIKELY_STOPPED_AFTER_REPLY_VAR_0}Re-arm it only if you have more to do before you reply; a few minutes after your reply a new watch is likely stopped, so tell the user what to check instead.]
