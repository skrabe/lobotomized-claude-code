<!--
name: Artifact Preview Consent Ask
description: >-
  checkPermissions ask message for previewing a local HTML page in a headless
  browser; on decline it becomes the tool_result the model reads.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_PREVIEW_CONSENT_ASK_VAR_0
-->
Claude wants to preview ${TOOL_RESULT_ARTIFACT_PREVIEW_CONSENT_ASK_VAR_0}: render it locally in a headless browser and return screenshots. Nothing is uploaded; the page may fetch Google Fonts stylesheets it references.
