<!--
name: 'Artifact Share: HTTP Failure'
description: >-
  Artifact share tool error for a non-5xx HTTP failure while reading or applying
  a share, without a retry hint.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_VAR_0
  - TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_VAR_1
-->
Couldn't ${TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_VAR_0==="write"?"apply the share":"read the artifact's sharing"} (HTTP ${TOOL_RESULT_ARTIFACT_SHARE_HTTP_FAILED_VAR_1.status}).
