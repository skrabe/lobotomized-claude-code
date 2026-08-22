<!--
name: 'Tool Result: Artifact live-edit certified-page check transient failure'
description: >-
  Error returned to the model when the Artifact live-edit certified-page
  precheck fails transiently and the call should be retried.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_LIVE_EDIT_CERTIFIED_CHECK_TRANSIENT_VAR_0
-->
live-edit refused: could not verify the target page is not a certified page (transient read failure: ${TOOL_RESULT_ARTIFACT_LIVE_EDIT_CERTIFIED_CHECK_TRANSIENT_VAR_0.err}). Retry the live-edit; if it persists, read the page (action: "read") to confirm it is reachable.
