<!--
name: 'Data: task notification queued agent message dropped'
description: >-
  Task-notification summary telling the coordinator that a queued message could
  not resume an agent and was dropped unread.
ccVersion: 2.1.331
variables:
  - DATA_TASK_NOTIFICATION_QUEUED_AGENT_MESSAGE_DROPPED_VAR_0
  - DATA_TASK_NOTIFICATION_QUEUED_AGENT_MESSAGE_DROPPED_VAR_1
-->
A message queued for agent ${DATA_TASK_NOTIFICATION_QUEUED_AGENT_MESSAGE_DROPPED_VAR_0} could not resume it and was dropped unread, so no notification will come for that message. ${DATA_TASK_NOTIFICATION_QUEUED_AGENT_MESSAGE_DROPPED_VAR_1.message}
