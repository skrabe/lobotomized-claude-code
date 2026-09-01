<!--
name: 'Task Notification: Agent Stop And Resume Note'
description: >-
  <note> block in the agent task-notification body injected into the
  orchestrator's context, explaining that a notification fires each time the
  agent stops and the same task-id may notify more than once.
ccVersion: 2.1.218
variables:
  - DATA_TASK_NOTIFICATION_AGENT_STOP_RESUME_NOTE_VAR_0
  - DATA_TASK_NOTIFICATION_AGENT_STOP_RESUME_NOTE_VAR_1
  - DATA_TASK_NOTIFICATION_AGENT_STOP_RESUME_NOTE_VAR_2
-->

<note>A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.</note>${DATA_TASK_NOTIFICATION_AGENT_STOP_RESUME_NOTE_VAR_0}${DATA_TASK_NOTIFICATION_AGENT_STOP_RESUME_NOTE_VAR_1}${DATA_TASK_NOTIFICATION_AGENT_STOP_RESUME_NOTE_VAR_2}
