<!--
name: 'Tool Result: Artifact content fetch denied by egress proxy'
description: >-
  Error reporting that the environment's egress proxy refused the direct
  claudeusercontent.com asset fetch, with HTTP status and proxy detail.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_CONTENT_EGRESS_DENIED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_CONTENT_EGRESS_DENIED_VAR_1
-->
artifact content fetch refused by the environment's egress proxy (HTTP ${TOOL_RESULT_ARTIFACT_ASSET_CONTENT_EGRESS_DENIED_VAR_0.status}: ${TOOL_RESULT_ARTIFACT_ASSET_CONTENT_EGRESS_DENIED_VAR_1})
