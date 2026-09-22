<!--
name: 'Artifact conflict — live content withheld, comment notification pending'
description: >-
  Conflict-publish tool_result explaining a pending comment notification
  withheld live content, so the model must read with consent or wait for the
  next typed user message.
ccVersion: 2.1.273
variables:
  - >-
    TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_COMMENT_NOTIFICATION_VAR_0
-->
 The live content was withheld here: a comment notification for this artifact is pending, so reading it needs the user's consent and a publish cannot ask for it. Read it with ${TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_COMMENT_NOTIFICATION_VAR_0} {action: "read"} (that read may ask first), or wait: the user's next message typed at the prompt usually lifts this hold. Re-saving your local file or stopping the watch does not.
