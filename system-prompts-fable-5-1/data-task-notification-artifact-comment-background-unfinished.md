<!--
name: 'Data: Task Notification Artifact Comment Background Agent Unfinished'
description: >-
  Main-session task notification when a background comment agent finished
  without reading a comment and no replacement fork could be started, telling
  the model to read the thread and act.
ccVersion: 2.1.269
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_3
-->
${DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_0({trigger:"fresh",summonCount:1,url:DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_1.url,threadId:DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_1.threadId})}. A background agent was handling this thread but finished without reading that comment, and no new agent could be started. Read the thread (${DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_2()}); answer any question in your reply, and if it asks for a change and the change is appropriate, make it.${DATA_TASK_NOTIFICATION_ARTIFACT_COMMENT_BACKGROUND_UNFINISHED_VAR_3()}
