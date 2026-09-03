<!--
name: 'Tool Result: Artifact DB Network-Off Read'
description: >-
  read_db error when the cloud session's network access is off, so reads cannot
  run here while writes may still work.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_DB_NETWORK_OFF_READ_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_NETWORK_OFF_READ_VAR_0}: this cloud session's network access is turned off (or could not be confirmed), so it cannot read artifact data — writes still work; do not retry the read here
