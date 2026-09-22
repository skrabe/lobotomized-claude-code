<!--
name: 'Tool Result: Artifact DB Network-Off Write'
description: >-
  write_db error when cloud network access is off and the gateway did not accept
  the write; do not retry here.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_DB_NETWORK_OFF_WRITE_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_NETWORK_OFF_WRITE_VAR_0}: this cloud session's network access is turned off (or could not be confirmed), and the gateway did not accept this call as a write it allows — do not retry it here
