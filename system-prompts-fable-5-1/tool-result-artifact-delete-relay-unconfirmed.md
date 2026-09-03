<!--
name: Artifact Delete Unconfirmed — Cloud Relay Failed
description: >-
  Artifact delete `{err}` from gxr() when the cloud relay failed, telling the
  model the delete may have gone through and to list before retrying.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_ARTIFACT_DELETE_RELAY_UNCONFIRMED_VAR_0
-->
Couldn't confirm the delete (the cloud relay failed: ${TOOL_RESULT_ARTIFACT_DELETE_RELAY_UNCONFIRMED_VAR_0}) — it may have gone through; check with action "list" before telling the user or trying again.
