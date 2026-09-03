<!--
name: Artifact db write outcome unknown — relay HTTP error
description: >-
  Artifact tool error telling Claude an artifact db write may have applied
  despite a relay HTTP failure, and to read back before retrying.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_DB_WRITE_RELAY_HTTP_UNKNOWN_VAR_0
-->
db write outcome unknown (relay HTTP ${TOOL_RESULT_ARTIFACT_DB_WRITE_RELAY_HTTP_UNKNOWN_VAR_0.status}) — it may have applied; read back before retrying
