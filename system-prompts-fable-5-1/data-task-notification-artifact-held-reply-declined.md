<!--
name: 'Data: Artifact Held Reply Declined'
description: >-
  Task notification injected when the user declines a drafted artifact comment
  reply and leaves feedback the session must act on.
ccVersion: 2.1.261
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_3
-->
The user declined a drafted reply to a comment thread on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_0.url} and said: "${DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_2.feedback)}". Act on that; replies to comments on this artifact will not be drafted for them again this session — use ${DATA_TASK_NOTIFICATION_ARTIFACT_HELD_REPLY_DECLINED_VAR_3()} to read and reply if they ask.
