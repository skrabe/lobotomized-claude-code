<!--
name: 'Data: Task notification artifact act then reply and resolve tail'
description: >-
  Tail instructing the session, once it has acted on an artifact comment thread,
  to check the thread first, post a brief reply saying what it did unless one
  already stands, and resolve the thread
ccVersion: 2.1.257
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_ACT_THEN_REPLY_AND_RESOLVE_TAIL_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_ACT_THEN_REPLY_AND_RESOLVE_TAIL_VAR_1
-->
 Once you have finished acting on the thread, post a brief reply saying what you did — first check the thread (${DATA_TASK_NOTIFICATION_ARTIFACT_ACT_THEN_REPLY_AND_RESOLVE_TAIL_VAR_0('action "comments"',()=>DATA_TASK_NOTIFICATION_ARTIFACT_ACT_THEN_REPLY_AND_RESOLVE_TAIL_VAR_1("comments"))}): if a Claude reply answering it already stands, do NOT post another — and resolve the thread (${DATA_TASK_NOTIFICATION_ARTIFACT_ACT_THEN_REPLY_AND_RESOLVE_TAIL_VAR_0('Artifact tool, action "resolve"',()=>DATA_TASK_NOTIFICATION_ARTIFACT_ACT_THEN_REPLY_AND_RESOLVE_TAIL_VAR_1("resolve"))}); leave it open only if the conversation is still active or the commenter still needs to read an answer from you.
