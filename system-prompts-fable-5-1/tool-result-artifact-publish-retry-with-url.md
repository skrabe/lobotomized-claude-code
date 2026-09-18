<!--
name: Artifact Publish Retry With Url
description: Retry clause when a cross-org publish was unasked and a retryUrl is known.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_RETRY_WITH_URL_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_RETRY_WITH_URL_VAR_1
-->
Retry publishing with url: ${TOOL_RESULT_ARTIFACT_PUBLISH_RETRY_WITH_URL_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_RETRY_WITH_URL_VAR_1.retryUrl)} so that question is asked.
