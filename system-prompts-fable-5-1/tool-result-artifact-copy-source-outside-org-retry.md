<!--
name: Artifact Copy Source Outside Org Retry
description: >-
  copy_source_outside_org_retry ArtifactInputError when a copied source's
  other-org ownership became clear after upload started; the earlier approval
  carries over.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_COPY_SOURCE_OUTSIDE_ORG_RETRY_VAR_0
  - TOOL_RESULT_ARTIFACT_COPY_SOURCE_OUTSIDE_ORG_RETRY_VAR_1
-->
${TOOL_RESULT_ARTIFACT_COPY_SOURCE_OUTSIDE_ORG_RETRY_VAR_0}, which only became clear after the upload started, so nothing was published yet. ${TOOL_RESULT_ARTIFACT_COPY_SOURCE_OUTSIDE_ORG_RETRY_VAR_1}. The earlier approval of that artifact carries over to the retry.
