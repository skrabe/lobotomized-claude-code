<!--
name: 'System Reminder: Artifact deleted by the user'
description: >-
  Meta message injected when the user deletes an artifact from /artifacts,
  telling the model the link is dead, cannot be restored or republished to, and
  that the url must not be passed to the Artifact tool
ccVersion: 2.1.239
variables:
  - SYSTEM_REMINDER_ARTIFACT_DELETED_BY_USER_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_DELETED_BY_USER_VAR_1
-->
<${SYSTEM_REMINDER_ARTIFACT_DELETED_BY_USER_VAR_0} url="${SYSTEM_REMINDER_ARTIFACT_DELETED_BY_USER_VAR_1}"/> The user deleted this Artifact from /artifacts: its link no longer works for anyone, it cannot be restored, and it cannot be published to again — publishing the same file creates a new Artifact at a new URL. Do not pass this url to the Artifact tool.
