<!--
name: 'Data: Task Notification Artifact Auto-Edit Thread Followup'
description: >-
  Injected for the model after an automatic artifact edit completes without a
  confirmed thread resolution and follow-up may be needed.
ccVersion: 2.1.257
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_THREAD_FOLLOWUP_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_THREAD_FOLLOWUP_VAR_1
-->
 The thread may not be resolved — check it (${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_THREAD_FOLLOWUP_VAR_0('action "comments"',()=>DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_THREAD_FOLLOWUP_VAR_1("comments"))}); if the change is right and the thread is still open, resolve it (${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_THREAD_FOLLOWUP_VAR_0('Artifact tool, action "resolve"',()=>DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_THREAD_FOLLOWUP_VAR_1("resolve"))}). Do NOT post another reply — the summary reply is already in the thread.
