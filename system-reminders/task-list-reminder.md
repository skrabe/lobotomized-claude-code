<!--
name: Task-list status reminder
description: >-
  Fires every turn while TaskList has entries. Wraps the current task list with
  reminder text about using TaskCreate. Empty .md = suppress entirely.
ccVersion: 2.1.291
placeholders:
  - existing_tasks
shadows:
  - system-reminder-task-tools-reminder
-->
{{existing_tasks}}
