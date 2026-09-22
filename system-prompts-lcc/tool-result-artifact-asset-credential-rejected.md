<!--
name: 'Tool Result: Artifact asset credential rejected'
description: >-
  Artifact asset error saying the server refused the session credential at the
  asset door and that this is an integration fault to report.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_CREDENTIAL_REJECTED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_CREDENTIAL_REJECTED_VAR_1
-->
${TOOL_RESULT_ARTIFACT_ASSET_CREDENTIAL_REJECTED_VAR_0}: the server refused this session's credential at the asset door — not an access or existence answer; report this as a client/server integration fault${TOOL_RESULT_ARTIFACT_ASSET_CREDENTIAL_REJECTED_VAR_1?` (${TOOL_RESULT_ARTIFACT_ASSET_CREDENTIAL_REJECTED_VAR_1})`:""}
