<!--
name: Asset call failed — invalid request
description: >-
  Artifact asset error arm for an invalid_request code, defaulting to a message
  that the server could not accept the request as shaped.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_INVALID_REQUEST_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_INVALID_REQUEST_VAR_1
-->
${TOOL_RESULT_ARTIFACT_ASSET_INVALID_REQUEST_VAR_0}: ${TOOL_RESULT_ARTIFACT_ASSET_INVALID_REQUEST_VAR_1??"the server could not accept the request as shaped"}
