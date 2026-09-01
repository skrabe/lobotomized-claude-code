<!--
name: Artifact Not Found Error
description: >-
  Error returned to the model that the artifact was not found, deleted, or not
  shared with it.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_NOT_FOUND_VAR_0
  - TOOL_RESULT_ARTIFACT_NOT_FOUND_VAR_1
-->
artifact not found — it may have been deleted, or it has not been shared with you${TOOL_RESULT_ARTIFACT_NOT_FOUND_VAR_0===void 0?"":`. If it is restricted to specific people, ${TOOL_RESULT_ARTIFACT_NOT_FOUND_VAR_1}`}
