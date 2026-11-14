<!--
name: 'System Reminder: Attached machines cloud container line'
description: >-
  Line describing the chat's own cloud container: user attachments and scratch
  work live there, it has none of the machine's files or hardware
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_ATTACHED_MACHINES_CLOUD_CONTAINER_LINE_VAR_0
  - SYSTEM_REMINDER_ATTACHED_MACHINES_CLOUD_CONTAINER_LINE_VAR_1
-->
- ${SYSTEM_REMINDER_ATTACHED_MACHINES_CLOUD_CONTAINER_LINE_VAR_0()}: this chat's own cloud container. What the user attached to this chat (under /mnt/user-data) and your scratch work are here; whether a tool of ${SYSTEM_REMINDER_ATTACHED_MACHINES_CLOUD_CONTAINER_LINE_VAR_1} can open an attached file shows when you try it. The container has none of that machine's files or hardware, and nothing moves between the two by itself.
