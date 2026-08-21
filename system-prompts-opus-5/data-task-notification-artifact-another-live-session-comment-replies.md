<!--
name: 'Data: Task Notification Artifact Another Live Session Comment Replies'
description: >-
  Task-notification body warning that another live session of the same
  conversation may also auto-reply to artifact comments.
ccVersion: 2.1.238
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_1
-->

<event>${DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_0(`Another live session of this same conversation is running. If it is also replying to comments on ${DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_1}, every comment will get a reply from both sessions until one stops. Tell the user; they can end either session's live-updates task in /tasks. Do not stop a watch on your own.`)}</event>
