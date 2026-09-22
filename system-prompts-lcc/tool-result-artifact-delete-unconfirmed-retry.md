<!--
name: Artifact delete not confirmed retry once
description: >-
  Delete failure text for a 5xx, telling the model the artifact may already be
  unreachable and the delete may be retried once.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_UNCONFIRMED_RETRY_VAR_0
-->
Couldn't confirm the delete (HTTP ${TOOL_RESULT_ARTIFACT_DELETE_UNCONFIRMED_RETRY_VAR_0.status}) — the Artifact may already be unreachable; retry once.
