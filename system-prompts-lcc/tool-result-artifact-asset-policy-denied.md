<!--
name: 'Tool Result: Artifact asset policy denied'
description: >-
  Artifact asset error for an organization artifact-policy block, defaulting to
  a generic policy sentence when the server gives no detail.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_POLICY_DENIED_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_POLICY_DENIED_VAR_1
-->
${TOOL_RESULT_ARTIFACT_ASSET_POLICY_DENIED_VAR_0}: ${TOOL_RESULT_ARTIFACT_ASSET_POLICY_DENIED_VAR_1??"blocked by the organization's artifact policy"}
