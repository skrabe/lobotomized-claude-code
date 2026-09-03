<!--
name: Asset call failed — too large
description: >-
  Artifact asset error arm for a too_large code, telling Claude the server or an
  intermediary rejected the file and to compress or split it.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_ASSET_TOO_LARGE_VAR_0
  - TOOL_RESULT_ARTIFACT_ASSET_TOO_LARGE_VAR_1
-->
${TOOL_RESULT_ARTIFACT_ASSET_TOO_LARGE_VAR_0}: ${TOOL_RESULT_ARTIFACT_ASSET_TOO_LARGE_VAR_1??"rejected as too large by the server or an intermediary although under the client limit — compress or split it"}
