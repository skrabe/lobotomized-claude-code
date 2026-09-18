<!--
name: Artifact Copy Source Owner Unconfirmed
description: >-
  copy_source_unconfirmed / copy_source_outside_org_retry ArtifactInputError
  when another copied source's owner could not be confirmed, so nothing was
  published.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_COPY_SOURCE_OWNER_UNCONFIRMED_VAR_0
  - TOOL_RESULT_ARTIFACT_COPY_SOURCE_OWNER_UNCONFIRMED_VAR_1
  - TOOL_RESULT_ARTIFACT_COPY_SOURCE_OWNER_UNCONFIRMED_VAR_2
-->
${TOOL_RESULT_ARTIFACT_COPY_SOURCE_OWNER_UNCONFIRMED_VAR_0}, and the owner of another copied source (${TOOL_RESULT_ARTIFACT_COPY_SOURCE_OWNER_UNCONFIRMED_VAR_1.join(", ")}) couldn't be confirmed, so nothing was published. ${TOOL_RESULT_ARTIFACT_COPY_SOURCE_OWNER_UNCONFIRMED_VAR_2} so those sources are checked again.
