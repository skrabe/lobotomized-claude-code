<!--
name: Org Policy HTTP Check Proxy
description: >-
  Artifact tool denial telling the model the org policy failed with an HTTP
  status and to check the proxy.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_CHECK_PROXY_VAR_0
  - TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_CHECK_PROXY_VAR_1
  - TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_CHECK_PROXY_VAR_2
-->
${TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_CHECK_PROXY_VAR_0}: your organization's policy couldn't be loaded from ${TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_CHECK_PROXY_VAR_1} (HTTP ${TOOL_RESULT_ARTIFACT_ORG_POLICY_HTTP_CHECK_PROXY_VAR_2}). Check your proxy settings.
