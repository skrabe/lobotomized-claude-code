<!--
name: 'Data: Task Notification Artifact Thread Resolve After Acting Tail'
description: >-
  Second half of the auto-posted-reply tail, telling the session to resolve the
  thread with the Artifact tool once it has finished acting and when to leave it
  open.
ccVersion: 2.1.257
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_THREAD_RESOLVE_AFTER_ACTING_TAIL_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_THREAD_RESOLVE_AFTER_ACTING_TAIL_VAR_1
-->
 Once you have finished acting on the thread, resolve it (${DATA_TASK_NOTIFICATION_ARTIFACT_THREAD_RESOLVE_AFTER_ACTING_TAIL_VAR_0('Artifact tool, action "resolve"',()=>DATA_TASK_NOTIFICATION_ARTIFACT_THREAD_RESOLVE_AFTER_ACTING_TAIL_VAR_1("resolve"))}); leave it open only if the conversation is still active or the commenter still needs an answer beyond the posted reply.
