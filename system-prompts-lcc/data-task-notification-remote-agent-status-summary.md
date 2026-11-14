<!--
name: 'Data: Task notification remote agent status summary'
description: >-
  Default summary in a remote-agent task notification saying the remote task
  completed, failed, is blocked or was stopped.
ccVersion: 2.1.325
variables:
  - DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_0
  - DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_1
  - DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_2
-->
${DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_0}${DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_1}" ${DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_2==="completed"?"completed successfully":DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_2==="failed"?"failed":DATA_TASK_NOTIFICATION_REMOTE_AGENT_STATUS_SUMMARY_VAR_2==="blocked"?"is blocked":"was stopped"}
