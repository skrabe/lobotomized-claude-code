<!--
name: 'Artifact Preview: Origin Load Not Taken In Preview'
description: >-
  Preview load issue that preview only fetches stylesheets and font files from
  that origin, so this request was skipped.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_PREVIEW_ORIGIN_STYLESHEETS_FONTS_ONLY_VAR_0
  - TOOL_RESULT_ARTIFACT_PREVIEW_ORIGIN_STYLESHEETS_FONTS_ONLY_VAR_1
-->
${TOOL_RESULT_ARTIFACT_PREVIEW_ORIGIN_STYLESHEETS_FONTS_ONLY_VAR_0(TOOL_RESULT_ARTIFACT_PREVIEW_ORIGIN_STYLESHEETS_FONTS_ONLY_VAR_1.url,120)} is not loaded in preview, which takes only stylesheets and font files from that origin (${TOOL_RESULT_ARTIFACT_PREVIEW_ORIGIN_STYLESHEETS_FONTS_ONLY_VAR_0(TOOL_RESULT_ARTIFACT_PREVIEW_ORIGIN_STYLESHEETS_FONTS_ONLY_VAR_1.type||"request",16)}); the published page may load it
