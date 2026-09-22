<!--
name: 'System Reminder: Artifact follow-up co-delivered to editor'
description: >-
  Tells the coordinator a thread follow-up was also delivered to the artifact
  editor worker, so it must not re-dispatch and should wait for that worker's
  next result.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_ARTIFACT_FOLLOW_UP_CODELIVERED_TO_EDITOR_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_FOLLOW_UP_CODELIVERED_TO_EDITOR_VAR_1
-->
[The thread follow-up${SYSTEM_REMINDER_ARTIFACT_FOLLOW_UP_CODELIVERED_TO_EDITOR_VAR_0?` "${SYSTEM_REMINDER_ARTIFACT_FOLLOW_UP_CODELIVERED_TO_EDITOR_VAR_0}"`:""} you just read (or will read next) was also delivered directly to the artifact editor worker ${SYSTEM_REMINDER_ARTIFACT_FOLLOW_UP_CODELIVERED_TO_EDITOR_VAR_1}, which is applying it now. Do not re-dispatch it. Reply with the link when that worker's NEXT result arrives; until then no_reply_needed (awaiting_worker_link).]
