<!--
name: Artifact fast-ack posted (plan mode)
description: >-
  Task notification that an acknowledgement reply was posted but automatic
  replies are paused in plan mode, so the full reply comes when the session next
  acts.
ccVersion: 2.1.233
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_FAST_ACK_PLAN_MODE_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_FAST_ACK_PLAN_MODE_VAR_1
-->
Acknowledgement reply posted to thread ${DATA_TASK_NOTIFICATION_ARTIFACT_FAST_ACK_PLAN_MODE_VAR_0.id} on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_FAST_ACK_PLAN_MODE_VAR_1}; automatic replies are paused (plan mode), so the full reply comes from this session when it next acts. When posting it, set acknowledge_duplicate: true — the acknowledgement already stands as the thread's reply, so the duplicate guard refuses a plain follow-up.
