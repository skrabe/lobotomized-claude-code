<!--
name: 'Data: MCP task monitoring result body'
description: >-
  Wraps the monitoring notice in a result block identifying the background task
  id and asking to name it by what the user asked for
ccVersion: 2.1.319
variables:
  - DATA_TASK_NOTIFICATION_MCP_TASK_MONITORING_RESULT_BODY_VAR_0
  - DATA_TASK_NOTIFICATION_MCP_TASK_MONITORING_RESULT_BODY_VAR_1
-->

<result>
${DATA_TASK_NOTIFICATION_MCP_TASK_MONITORING_RESULT_BODY_VAR_0}
Which task this is: the background task with the id ${DATA_TASK_NOTIFICATION_MCP_TASK_MONITORING_RESULT_BODY_VAR_1}. Name it to the user by what they asked for, not by this id.
</result>
