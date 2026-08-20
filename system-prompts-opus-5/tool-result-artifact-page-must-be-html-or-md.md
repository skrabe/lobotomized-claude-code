<!--
name: 'Tool Result: Artifact Page Must Be HTML or Markdown'
description: >-
  Rejection when a non-page file is published except onto an Artifact created
  from an Artifact type (optionally suggesting `type_url`).
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_PAGE_MUST_BE_HTML_OR_MD_VAR_0
  - TOOL_RESULT_ARTIFACT_PAGE_MUST_BE_HTML_OR_MD_VAR_1
-->
an Artifact's page must be .html or .md — other files publish only to an Artifact created from an Artifact type: pass that Artifact's \`url\` (you must be able to edit it)${TOOL_RESULT_ARTIFACT_PAGE_MUST_BE_HTML_OR_MD_VAR_0().frozenArtifactTypes?.TOOL_RESULT_ARTIFACT_PAGE_MUST_BE_HTML_OR_MD_VAR_1===!0?", or `type_url` to create a new one":""}
