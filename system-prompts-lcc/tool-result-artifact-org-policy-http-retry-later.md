<!--
name: Org Policy HTTP Retry Later
description: >-
  Artifact tool denial telling the model the org policy failed with HTTP 429 or
  5xx and to try later.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_RETRY_LATER_VAR_0
  - TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_RETRY_LATER_VAR_1
  - TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_RETRY_LATER_VAR_2
-->
${TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_RETRY_LATER_VAR_0}: your organization's policy couldn't be loaded from ${TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_RETRY_LATER_VAR_1} (HTTP ${TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_RETRY_LATER_VAR_2}). Try again later.
