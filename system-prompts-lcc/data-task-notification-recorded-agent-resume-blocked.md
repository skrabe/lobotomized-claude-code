<!--
name: 'Data: Task notification recorded agent resume blocked'
description: Says the session's permission rules now block resuming this agent
ccVersion: 2.1.330
variables:
  - DATA_TASK_NOTIFICATION_RECORDED_AGENT_RESUME_BLOCKED_VAR_0
  - DATA_TASK_NOTIFICATION_RECORDED_AGENT_RESUME_BLOCKED_VAR_1
-->
This session's permission rules now block this agent's type${DATA_TASK_NOTIFICATION_RECORDED_AGENT_RESUME_BLOCKED_VAR_0===void 0?"":", its model or a background agent,"} or require approval for ${DATA_TASK_NOTIFICATION_RECORDED_AGENT_RESUME_BLOCKED_VAR_0===void 0?"it":"one of them"}${DATA_TASK_NOTIFICATION_RECORDED_AGENT_RESUME_BLOCKED_VAR_1?"":", or background agents are off"}.
