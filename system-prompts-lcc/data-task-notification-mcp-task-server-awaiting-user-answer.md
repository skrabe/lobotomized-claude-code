<!--
name: 'MCP task: server awaiting user answer'
description: >-
  Task notification body telling the model the task's server waits for a user
  answer and how to surface it.
ccVersion: 2.1.331
variables:
  - DATA_TASK_NOTIFICATION_MCP_TASK_SERVER_AWAITING_USER_ANSWER_VAR_0
  - DATA_TASK_NOTIFICATION_MCP_TASK_SERVER_AWAITING_USER_ANSWER_VAR_1
-->

<result>
This task's server is waiting for the user to answer a question. Only the user can see and answer it. Tell the user in one sentence that the task has a question, then call the ${DATA_TASK_NOTIFICATION_MCP_TASK_SERVER_AWAITING_USER_ANSWER_VAR_0} tool (task_id: ${DATA_TASK_NOTIFICATION_MCP_TASK_SERVER_AWAITING_USER_ANSWER_VAR_1}) to show it to them. The call can wait until the user is back, so unless they have just written, first finish the work that does not need the answer. If you cannot call the tool now, ask the user to reply here, and call it after their reply. Name the task by what they asked for, and leave out its id.
</result>
