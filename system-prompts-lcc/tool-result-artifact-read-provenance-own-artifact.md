<!--
name: 'Artifact read provenance: user''s own artifact'
description: >-
  Provenance lead for content of the user's own artifact naming who else may
  have written it.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_2
-->
${TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_0} of the user's own artifact that ${TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_1.typeLocked?`its Artifact type's publisher${TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_2?" or a writer outside the user's organization":TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_1.cowritten?" or another writer":""}`:TOOL_RESULT_ARTIFACT_READ_PROVENANCE_OWN_ARTIFACT_VAR_2?"a writer outside the user's organization":"another writer of the artifact"} may have written
