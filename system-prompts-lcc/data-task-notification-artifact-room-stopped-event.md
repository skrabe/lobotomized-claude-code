<!--
name: 'Data: Artifact Room Stopped Event'
description: >-
  Task-notification <event> body reporting that live rooms were left or that no
  room was open after the user stopped background activity.
ccVersion: 2.1.246
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_STOPPED_EVENT_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_STOPPED_EVENT_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_STOPPED_EVENT_VAR_2
-->

<event>${DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_STOPPED_EVENT_VAR_0(DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_STOPPED_EVENT_VAR_1>0?`Page events from those artifacts' viewers will no longer arrive and room_send to them will report not_connected; every remembered room-join approval was forgotten too. ${DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_STOPPED_EVENT_VAR_2}`:`No room was open. ${DATA_TASK_NOTIFICATION_ARTIFACT_ROOM_STOPPED_EVENT_VAR_2}`)}</event>
