<!--
name: 'Artifact Preview: Theme-Only Color Variables'
description: >-
  Static preview issue listing color variables set only inside
  prefers-color-scheme or data-theme blocks.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_PREVIEW_THEME_ONLY_COLOR_VAR_0
  - TOOL_RESULT_ARTIFACT_PREVIEW_THEME_ONLY_COLOR_VAR_1
-->
${TOOL_RESULT_ARTIFACT_PREVIEW_THEME_ONLY_COLOR_VAR_0.join(", ")} ${TOOL_RESULT_ARTIFACT_PREVIEW_THEME_ONLY_COLOR_VAR_1(TOOL_RESULT_ARTIFACT_PREVIEW_THEME_ONLY_COLOR_VAR_0.length,"is","are")} set only inside @media (prefers-color-scheme) or [data-theme] blocks, so ${TOOL_RESULT_ARTIFACT_PREVIEW_THEME_ONLY_COLOR_VAR_1(TOOL_RESULT_ARTIFACT_PREVIEW_THEME_ONLY_COLOR_VAR_0.length,"it is","they are")} unset in the other theme
