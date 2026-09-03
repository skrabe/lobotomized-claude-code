<!--
name: Artifact Thumbnail Bad Media Attribute
description: >-
  Preview/publish problem that artifact-thumbnail media is not the allowed
  dark-mode value.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_BAD_MEDIA_VAR_0
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_BAD_MEDIA_VAR_1
-->
a <link rel="artifact-thumbnail"> tag has media=${TOOL_RESULT_ARTIFACT_THUMBNAIL_BAD_MEDIA_VAR_0(TOOL_RESULT_ARTIFACT_THUMBNAIL_BAD_MEDIA_VAR_1.badMedia)}; the only media value allowed is "(prefers-color-scheme: dark)" (for the dark-mode variant) — remove or fix the attribute
