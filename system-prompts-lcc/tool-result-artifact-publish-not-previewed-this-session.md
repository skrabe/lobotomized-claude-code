<!--
name: Artifact Publish Not Previewed This Session
description: >-
  Publish tool_result paragraph when previewHint is set, telling the model to
  preview the file for layout errors before viewers see it.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_NOT_PREVIEWED_THIS_SESSION_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_NOT_PREVIEWED_THIS_SESSION_VAR_1
-->


Not previewed this session: ${TOOL_RESULT_ARTIFACT_PUBLISH_NOT_PREVIEWED_THIS_SESSION_VAR_0('action "preview"',()=>`the \`${TOOL_RESULT_ARTIFACT_PUBLISH_NOT_PREVIEWED_THIS_SESSION_VAR_1}\` tool's preview`)} on this file catches layout and load errors before viewers see them; capability calls work only once published, so test those on the published page.
