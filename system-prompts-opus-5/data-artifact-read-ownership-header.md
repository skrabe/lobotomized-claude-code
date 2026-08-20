<!--
name: 'Data: Artifact Read Ownership Header'
description: >-
  Ownership phrase in the [Artifact …] header of the artifact-read tool result,
  including private/shared audience and type-locked or cowritten qualifiers.
ccVersion: 2.1.237
variables:
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_1
  - DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_2
-->
owned by you${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audience===void 0?"":DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audience==="owner"?", private":`, shared with ${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_1(DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audience)}${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audienceView===void 0?"":` (${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_2(DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.audienceView)})`}`}${DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.typeLocked?"; the page comes from its Artifact type and was written by the type's publisher":DATA_ARTIFACT_READ_OWNERSHIP_HEADER_VAR_0.cowritten?"; includes contributions from other writers":""}
