<!--
name: 'System Reminder: Artifact editor follow-up cancelled'
description: >-
  Coordinator note that a thread follow-up was cancelled, with reached vs
  withdrawn variants.
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_1
  - SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_2
-->
If you saw a note saying the artifact editor worker ${SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_0} is applying ${SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_1("")}, this concerns the thread follow-up that was just cancelled: ${SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_2?`it was cancelled from the thread after it had already reached ${SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_0}; if its result arrives, treat it as superseded by the cancellation (do not post it as the answer unless the thread asks again).`:`it was cancelled from the thread and withdrawn before ${SYSTEM_REMINDER_ARTIFACT_EDITOR_FOLLOW_UP_CANCELLED_VAR_0} read it — nothing is pending from it; do not wait for a result and do not dispatch it.`}
