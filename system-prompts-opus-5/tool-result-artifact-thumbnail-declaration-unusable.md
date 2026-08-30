<!--
name: 'Tool Result: Artifact Thumbnail Declaration Unusable'
description: >-
  Permission-deny message when a page's custom thumbnail tag cannot be
  published, so nothing was published.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_DECLARATION_UNUSABLE_VAR_0
-->
The page's custom thumbnail declaration cannot be used: ${TOOL_RESULT_ARTIFACT_THUMBNAIL_DECLARATION_UNUSABLE_VAR_0.problems.join("; ")}. Nothing was published — fix the <link rel="artifact-thumbnail"> tag (or remove it) and publish again.
