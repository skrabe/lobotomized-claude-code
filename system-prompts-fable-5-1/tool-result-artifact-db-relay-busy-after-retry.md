<!--
name: 'Tool Result: Artifact DB Relay Busy After Retry'
description: >-
  ArtifactData error returned when the cloud session's artifact connection was
  still unavailable after one retry. For a write it warns the edit may have
  applied and says to read it back before retrying; otherwise it says nothing
  ran and to retry shortly.
ccVersion: 2.1.277
variables:
  - TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_2
  - TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_3
  - TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_4
  - TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_5
-->
db ${TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_0} failed (${TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_1("store_unavailable")}): ${TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_2?"resolving 'me' failed — ":""}this cloud session's artifact connection was temporarily unavailable (HTTP ${TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_3.status}, after one retry); ${TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_4?"the edit may or may not have applied — read it back before retrying":`this is transient and nothing ran — retry shortly${TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_0==="write"?TOOL_RESULT_ARTIFACT_DB_RELAY_BUSY_AFTER_RETRY_VAR_5:""}`}
