<!--
name: Artifact read action description
description: >-
  Per-call description for action "read": reads a published artifact's content
  into the conversation, flagged when requested after an unattended auto-reply
  notification.
ccVersion: 2.1.239
variables:
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_3
-->
Read a published artifact's content into the conversation (read-only)${TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_0(TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_1)}${TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_2!==null&&TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_3(TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_2.slug)?" — requested after an unattended auto-reply notification":""}.
