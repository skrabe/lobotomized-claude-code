<!--
name: 'Artifact Share: HTTP Failure (Retry)'
description: >-
  Artifact share tool error for an HTTP 5xx while reading or applying a share,
  telling Claude to retry once.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_RETRY_VAR_0
  - TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_RETRY_VAR_1
-->
Couldn't ${TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_RETRY_VAR_0==="write"?"apply the share":"read the artifact's sharing"} (HTTP ${TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_RETRY_VAR_1.status}); retry once.
