<!--
name: 'Tool Description: Task Background Subagent Notification'
description: >-
  Conditional bullet in the Task/Agent tool description telling the model that
  subagents run in the background and that it must never fabricate a pending
  agent's results; injected as part of the Task tool's description field.
ccVersion: 2.1.325
variables:
  - TOOL_DESCRIPTION_TASK_BACKGROUND_SUBAGENT_NOTIFICATION_VAR_0
-->

- Subagents run in the background; you'll be notified when one completes.${TOOL_DESCRIPTION_TASK_BACKGROUND_SUBAGENT_NOTIFICATION_VAR_0}
