<!--
name: 'Data: Task Notification Artifact Resolve After Promised Reply Tail'
description: >-
  Tail instructing the session to resolve the artifact comment thread once the
  promised reply is posted, and when to leave it open instead.
ccVersion: 2.1.257
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_RESOLVE_AFTER_PROMISED_REPLY_TAIL_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_RESOLVE_AFTER_PROMISED_REPLY_TAIL_VAR_1
-->
 Once the promised reply is posted, resolve the thread (${DATA_TASK_NOTIFICATION_ARTIFACT_RESOLVE_AFTER_PROMISED_REPLY_TAIL_VAR_0('Artifact tool, action "resolve"',()=>DATA_TASK_NOTIFICATION_ARTIFACT_RESOLVE_AFTER_PROMISED_REPLY_TAIL_VAR_1("resolve"))}); leave it open only if the conversation is still active or the commenter still needs to read an answer from you.
