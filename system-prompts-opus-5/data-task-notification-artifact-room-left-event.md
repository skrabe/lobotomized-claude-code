<!--
name: 'Data: Artifact Room Left Event Envelope'
description: >-
  Task-notification <event> body wrapping the room-leave explanation after live
  artifact rooms are disposed.
ccVersion: 2.1.238
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_LEFT_EVENT_VAR_0
-->

<event>${DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_LEFT_EVENT_VAR_0("Page events from those artifacts' viewers will no longer arrive and room_send to them will report not_connected. Do not republish to rejoin unless the user asks.")}</event>
