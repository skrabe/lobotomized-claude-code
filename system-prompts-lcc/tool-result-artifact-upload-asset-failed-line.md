<!--
name: Artifact Upload Asset Failed Line
description: >-
  Per-file failure line on the upload_asset tool_result with status and
  truncated message.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_0
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_1
  - TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_2
-->
- ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_0}: ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_1.status==="not_attempted"?"not attempted":TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_1.may_be_stored===!0?"failed, but may be stored":"failed"} — ${TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_2(TOOL_RESULT_ARTIFACT_UPLOAD_ASSET_FAILED_LINE_VAR_1.message,1024)}
