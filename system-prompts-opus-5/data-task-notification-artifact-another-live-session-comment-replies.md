<!--
name: 'Task Notification: Artifact Another Live Session Comment Replies'
description: >-
  Reports how concurrent live sessions resolved or may duplicate automatic
  replies to comments on the same Artifact.
ccVersion: 2.1.246
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_3
-->

<event>${DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_0(DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_1?`Another live session of this same conversation was also armed to reply to comments on ${DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_2}; it paused its replies at this session's request, so only this session answers them now. Nothing to do; do not stop a watch on your own.`:DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_3?`Another live session of this same conversation claimed the replies to comments on ${DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_2} a moment after this one; this session paused its own at that session's request, so only that session answers them now. Nothing to do — a publish the user asks for here takes them back; do not republish or stop a watch on your own.`:`Another live session of this same conversation is running. If it is also replying to comments on ${DATA_TASK_NOTIFICATION_ARTIFACT_ANOTHER_LIVE_SESSION_COMMENT_REPLIES_VAR_2}, every comment will get a reply from both sessions until one stops. Tell the user; they can end either session's live-updates task in /tasks. Do not stop a watch on your own.`)}</event>
