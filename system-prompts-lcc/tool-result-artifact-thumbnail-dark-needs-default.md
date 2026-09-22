<!--
name: Artifact Dark Thumbnail Needs Default Link
description: >-
  Preview/publish problem that a dark-mode thumbnail requires a default
  artifact-thumbnail <link> as well.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_DARK_NEEDS_DEFAULT_VAR_0
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_DARK_NEEDS_DEFAULT_VAR_1
-->
a dark-mode thumbnail (media="(prefers-color-scheme: dark)") needs a default <link rel="artifact-thumbnail"> as well — add one without a media attribute${TOOL_RESULT_ARTIFACT_THUMBNAIL_DARK_NEEDS_DEFAULT_VAR_0.pastWindow?`, within the first ${TOOL_RESULT_ARTIFACT_THUMBNAIL_DARK_NEEDS_DEFAULT_VAR_1} characters (the one further down does not count)`:""}${TOOL_RESULT_ARTIFACT_THUMBNAIL_DARK_NEEDS_DEFAULT_VAR_0.oversizeTag?" (the over-long tag that was not read does not count)":""}
