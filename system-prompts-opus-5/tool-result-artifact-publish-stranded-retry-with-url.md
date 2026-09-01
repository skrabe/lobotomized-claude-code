<!--
name: Artifact Publish Stranded Retry With Url
description: >-
  Suffix on a publish ArtifactInputError telling the model to republish with the
  stranded slug and a favicon.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_STRANDED_RETRY_WITH_URL_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_STRANDED_RETRY_WITH_URL_VAR_1
-->
 Publish again with url: "${TOOL_RESULT_ARTIFACT_PUBLISH_STRANDED_RETRY_WITH_URL_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_STRANDED_RETRY_WITH_URL_VAR_1.strandedSlug)}" and a favicon to complete that artifact; publishing without the url creates a second one.
