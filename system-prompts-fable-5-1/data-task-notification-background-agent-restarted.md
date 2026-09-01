<!--
name: 'Task Notification: Background Agent Restarted From Transcript'
description: >-
  Message injected via H_r/ud with mode:'task-notification' into a
  <notification> block telling the model a background agent was auto-restarted
  from its saved transcript.
ccVersion: 2.1.199
variables:
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENT_RESTARTED_VAR_0
  - DATA_TASK_NOTIFICATION_BACKGROUND_AGENT_RESTARTED_VAR_1
-->
Background agent "${DATA_TASK_NOTIFICATION_BACKGROUND_AGENT_RESTARTED_VAR_0(DATA_TASK_NOTIFICATION_BACKGROUND_AGENT_RESTARTED_VAR_1.description)}" had no completion record after the previous Claude Code process exited, and was automatically restarted from its saved transcript. It is running in the background again; its result will arrive as a separate task notification.
