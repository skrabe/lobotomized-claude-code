<!--
name: Artifact Delete Unconfirmed — Foreign OK
description: >-
  Artifact delete `{err}` when a non-204 or relayed response was not the
  Artifact service's own, so the Artifact may still be online.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_OK_FOREIGN_VAR_0
-->
Couldn't confirm the delete: the answer (HTTP ${TOOL_RESULT_ARTIFACT_DELETE_OK_FOREIGN_VAR_0.status}) was not the Artifact service's own, so the Artifact may still be online — check the Artifacts list again before treating it as deleted.
