<!--
name: Artifact Publish Deploy 422 Capability Refused
description: >-
  Publish tool error that wraps an HTTP 422 capability refusal, joining the
  named capability problems with the instruction to fix them and publish again.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_2
  - TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_3
-->
deploy 422: ${TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_0([TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_1,...TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_2].join("; "),["Nothing was published; fix each capabilities entry named — drop the unavailable ones, correct the others as described — and publish again.",...TOOL_RESULT_ARTIFACT_PUBLISH_DEPLOY_422_CAPABILITY_REFUSED_VAR_3].join(" Also: "))}
