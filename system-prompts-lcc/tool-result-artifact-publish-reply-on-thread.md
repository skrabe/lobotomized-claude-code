<!--
name: 'Tool Result: Artifact Publish Reply On Thread'
description: >-
  Publish tool-result addendum telling the model to also reply on the seeded
  comment thread so the commenter is notified.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_REPLY_ON_THREAD_VAR_0
-->
This publish responds to the comment sent to you on thread ${TOOL_RESULT_ARTIFACT_PUBLISH_REPLY_ON_THREAD_VAR_0}. Reply on that thread too (action "reply", this url, thread_id "${TOOL_RESULT_ARTIFACT_PUBLISH_REPLY_ON_THREAD_VAR_0}") so the commenter is notified — republishing the artifact does not notify them, even if you also answer in this session.
