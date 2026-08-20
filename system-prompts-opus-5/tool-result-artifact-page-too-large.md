<!--
name: 'Tool Result: Artifact Page Too Large'
description: >-
  Size-cap error from Czf telling the model the page exceeded the MB limit and
  to shrink or split it before retrying.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_PAGE_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_PAGE_TOO_LARGE_VAR_1
  - TOOL_RESULT_ARTIFACT_PAGE_TOO_LARGE_VAR_2
-->
too large: ${TOOL_RESULT_ARTIFACT_PAGE_TOO_LARGE_VAR_0.ceil(TOOL_RESULT_ARTIFACT_PAGE_TOO_LARGE_VAR_1/1024/1024)}MB (max ${TOOL_RESULT_ARTIFACT_PAGE_TOO_LARGE_VAR_2/1024/1024}MB). Shrink the page — move large inline assets (base64 images, embedded datasets) out of it or split the content across several artifacts — then retry.
