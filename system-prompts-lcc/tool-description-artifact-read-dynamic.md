<!--
name: 'Tool Description: Artifact read dynamic'
description: >-
  Per-call description for the artifact read action: the version-read text or
  the default read text, plus the unattended auto-reply notification suffix
ccVersion: 2.1.292
variables:
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_3
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_4
  - TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_5
-->
${TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_0(TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_1.version)??"Read a published artifact's content into the conversation (read-only)"}${TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_2(TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_3)}${TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_4!==null&&TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_5(TOOL_DESCRIPTION_ARTIFACT_READ_DYNAMIC_VAR_4.slug)?" — requested after an unattended auto-reply notification":""}.
