<!--
name: 'Tool Result: Artifact live-edit certified-page check read denied'
description: >-
  Error returned to the model when Artifact live-edit cannot read the target
  page to prove it is not a certified page and the HTTP status is non-transient.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_LIVE_EDIT_CERTIFIED_CHECK_READ_DENIED_VAR_0
-->
live-edit refused: could not verify the target page is not a certified page (read denied: ${TOOL_RESULT_ARTIFACT_LIVE_EDIT_CERTIFIED_CHECK_READ_DENIED_VAR_0.err}). An HTTP ${TOOL_RESULT_ARTIFACT_LIVE_EDIT_CERTIFIED_CHECK_READ_DENIED_VAR_0.status} failure is not transient, so retrying this live-edit cannot succeed — read the page (action: "read") to check its state.
