<!--
name: 'Data: Task Notification Agent Stop Resume Note'
description: >-
  Note in an agent-stop task-notification that the same task-id may notify more
  than once if the user resumes it.
ccVersion: 2.1.274
-->
A task-notification fires each time this agent stops with no live background children of its own. The user can send it another message and resume it, so the same task-id may notify more than once.
